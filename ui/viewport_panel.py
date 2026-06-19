import ttkbootstrap as ttk

from core.constants import *
from core.context import context
from core.selection.selection_mapper import SelectionMapper


class ViewportPanel(ttk.Frame):

    def __init__(self, master, context=None):

        super().__init__(master)

        self.context = context
        if context:
            self.event_bus = context.event_bus
        else:
            self.event_bus = None

        self.picker = None
        self.model_actor = None
        self.vtk_widget = None
        self.renderer = None
        self.render_window = None
        self.interactor = None
        self.vtk_available = False

        try:
            self.setup_ui()
            self.setup_vtk()
            self.setup_scene()
            self.vtk_available = True
        except Exception as e:
            # VTK not available, create canvas-based viewport
            import tkinter as tk
            self.canvas = tk.Canvas(self, bg="black", width=400, height=300)
            self.canvas.pack(fill="both", expand=True)
            self._draw_placeholder_grid()
            self.vtk_available = False
            
        if self.vtk_available:
            self.bind_events()

    ########################################################

    def _draw_placeholder_grid(self):
        """Draw a simple grid in the canvas"""
        # Draw grid lines
        for i in range(0, 400, 50):
            self.canvas.create_line(i, 0, i, 300, fill="gray30")
        for i in range(0, 300, 50):
            self.canvas.create_line(0, i, 400, i, fill="gray30")
        
        # Draw center axes
        self.canvas.create_line(200, 0, 200, 300, fill="red", width=2)
        self.canvas.create_line(0, 150, 400, 150, fill="green", width=2)
        
        # Draw placeholder text
        self.canvas.create_text(200, 30, text="3D Viewport (Mock)", fill="white", font=("Arial", 14))
        self.canvas.create_text(200, 150, text="Model will appear here", fill="gray", font=("Arial", 12))

    ########################################################

    def draw_model_shape(self, name, params):
        """Draw a mock 3D representation of the model"""
        if not hasattr(self, 'canvas'):
            return
            
        self.canvas.delete("all")
        
        # Draw background
        self.canvas.create_rectangle(0, 0, 400, 300, fill="black")
        
        # Draw grid
        for i in range(0, 400, 50):
            self.canvas.create_line(i, 0, i, 300, fill="gray30")
        for i in range(0, 300, 50):
            self.canvas.create_line(0, i, 400, i, fill="gray30")
        
        # Draw center axes
        self.canvas.create_line(200, 0, 200, 300, fill="red", width=2)
        self.canvas.create_line(0, 150, 400, 150, fill="green", width=2)
        
        # Draw model representation as 3D-like box
        width = params.get("Width", 100)
        depth = params.get("Depth", 100)
        height = params.get("Height", 20)
        
        # Scale to fit canvas
        scale = min(150 / max(width, depth, height, 1), 1.5)
        w = width * scale * 0.8
        d = depth * scale * 0.8
        h = height * scale * 0.6
        
        # Isometric view
        center_x, center_y = 200, 150
        
        # Draw 3D box (isometric)
        # Front face
        self.canvas.create_rectangle(
            center_x - w/2, center_y - h/2,
            center_x + w/2, center_y + h/2,
            fill="steelblue", outline="white", width=2
        )
        
        # Top face (isometric)
        offset_x = d * 0.3
        offset_y = d * 0.2
        self.canvas.create_polygon(
            center_x - w/2, center_y - h/2,
            center_x - w/2 + offset_x, center_y - h/2 - offset_y,
            center_x + w/2 + offset_x, center_y - h/2 - offset_y,
            center_x + w/2, center_y - h/2,
            fill="skyblue", outline="white", width=1
        )
        
        # Draw text
        self.canvas.create_text(200, 30, text=f"Model: {name}", fill="white", font=("Arial", 12, "bold"))
        dims_text = f"W:{width:.0f} D:{depth:.0f} H:{height:.0f}"
        self.canvas.create_text(200, 280, text=dims_text, fill="gray", font=("Arial", 10))

    ########################################################

    def setup_ui(self):
        import vtk
        from vtk.tk.vtkTkRenderWindowInteractor import vtkTkRenderWindowInteractor

        self.vtk_widget = vtkTkRenderWindowInteractor(self)
        self.vtk_widget.pack(fill="both", expand=True)

    ########################################################

    def setup_vtk(self):
        import vtk

        self.picker = vtk.vtkPropPicker()
        self.renderer = vtk.vtkRenderer()
        self.renderer.SetBackground(0.1, 0.1, 0.1)

        self.render_window = self.vtk_widget.GetRenderWindow()
        self.render_window.AddRenderer(self.renderer)

        self.interactor = self.render_window.GetInteractor()
        self.interactor.SetInteractorStyle(
            vtk.vtkInteractorStyleTrackballCamera()
        )

        # CLICK EVENT
        self.interactor.AddObserver(
            "LeftButtonPressEvent",
            self.on_left_click
        )

    ########################################################

    def setup_scene(self):

        if not self.vtk_available:
            return
        self.add_grid()
        self.add_axes()

    ########################################################

    def add_grid(self):

        import vtk
        plane = vtk.vtkPlaneSource()
        plane.SetXResolution(10)
        plane.SetYResolution(10)
        plane.SetOrigin(-100, -100, 0)
        plane.SetPoint1(100, -100, 0)
        plane.SetPoint2(-100, 100, 0)

        mapper = vtk.vtkPolyDataMapper()
        mapper.SetInputConnection(plane.GetOutputPort())

        actor = vtk.vtkActor()
        actor.SetMapper(mapper)
        actor.GetProperty().SetRepresentationToWireframe()
        actor.GetProperty().SetColor(0.3, 0.3, 0.3)

        self.renderer.AddActor(actor)

    ########################################################

    def add_axes(self):

        import vtk
        axes = vtk.vtkAxesActor()

        widget = vtk.vtkOrientationMarkerWidget()
        widget.SetOrientationMarker(axes)
        widget.SetInteractor(self.interactor)
        widget.SetViewport(0.0, 0.0, 0.2, 0.2)
        widget.SetEnabled(1)
        widget.InteractiveOn()

    ########################################################

    def bind_events(self):

        if not self.vtk_available or not self.event_bus:
            return
        self.event_bus.subscribe(
            MODEL_GENERATED,
            self.on_model_generated
        )

    ########################################################

    def on_model_generated(self, data):

        if not self.vtk_available:
            # Use canvas mock display
            if hasattr(self, 'canvas'):
                self.draw_model_shape(
                    data.get("name", "Model"),
                    data.get("parameters", {})
                )
            return
            
        stl_path = self.context.design_state.stl_file

        if stl_path:
            self.load_stl(stl_path)

    ########################################################

    def load_stl(self, path):

        if not self.vtk_available:
            return
        import vtk
        reader = vtk.vtkSTLReader()
        reader.SetFileName(path)
        reader.Update()

        mapper = vtk.vtkPolyDataMapper()
        mapper.SetInputConnection(reader.GetOutputPort())

        actor = vtk.vtkActor()
        actor.SetMapper(mapper)
        actor.GetProperty().SetColor(0.8, 0.8, 0.9)

        if self.model_actor:
            self.renderer.RemoveActor(self.model_actor)

        self.model_actor = actor
        self.renderer.AddActor(actor)

        self.renderer.ResetCamera()
        self.render_window.Render()

    ########################################################

    def on_left_click(self, obj, event):

        if not self.vtk_available:
            return
        click_pos = self.interactor.GetEventPosition()

        self.picker.Pick(
            click_pos[0],
            click_pos[1],
            0,
            self.renderer
        )

        actor = self.picker.GetActor()

        if actor and actor == self.model_actor:

            self.context.logger.info("Model clicked")

            self.context.selection_manager.set_selection(
                actor,
                {"type": "model"}
            )

            self.highlight(actor)

        else:

            self.context.selection_manager.clear_selection()

        return

    ########################################################

    def highlight(self, actor):

        if not self.vtk_available:
            return
        actor.GetProperty().SetColor(1.0, 0.5, 0.1)

        self.render_window.Render()

    ########################################################

    def refresh(self):

        if not self.vtk_available:
            return
        self.render_window.Render()

    def update_live_model(self, model):

        if not self.vtk_available:
            return
        self.context.logger.info("Live viewport update")

        stl_path = self.context.export_service.export_stl(model)

        self.load_stl(stl_path)