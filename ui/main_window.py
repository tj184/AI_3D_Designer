import ttkbootstrap as ttk

from config import *
from core.logger import logger

from ui.toolbar import Toolbar
from ui.statusbar import StatusBar
from ui.chat_panel import ChatPanel
from ui.parameter_panel import ParameterPanel
from ui.viewport_panel import ViewportPanel
from models.design_state import design_state

from core.constants import *


class MainWindow:

    def __init__(self, root, context):

        self.root = root
        self.context = context
        self.event_bus = context.event_bus

        self.root.title(APP_NAME)

        self.root.geometry(f"{WINDOW_WIDTH}x{WINDOW_HEIGHT}")

        self.root.minsize(
            MIN_WINDOW_WIDTH,
            MIN_WINDOW_HEIGHT
        )

        logger.info("Application Started")

        self.create_layout()

    ######################################################

    def create_layout(self):

        # ==================================================
        # Toolbar
        # ==================================================

        self.toolbar = Toolbar(
    self.root,
    self.context
)

        # ==================================================
        # Main Horizontal Split
        # ==================================================

        self.main = ttk.PanedWindow(
            self.root,
            orient="horizontal"
        )

        self.main.pack(
            fill="both",
            expand=True
        )

        # ==================================================
        # Chat Frame
        # ==================================================

        self.chat_frame = ttk.Labelframe(
            self.main,
            text="AI Assistant",
            width=CHAT_WIDTH
        )

        # ==================================================
        # Center Split
        # ==================================================

        self.center = ttk.PanedWindow(
            self.main,
            orient="horizontal"
        )

        # ==================================================
        # Parameter Frame
        # ==================================================

        self.parameter_frame = ttk.Labelframe(
            self.center,
            text="Parameters",
            width=PARAMETER_WIDTH
        )

        # ==================================================
        # Viewport Frame
        # ==================================================

        self.viewport_frame = ttk.Frame(
        self.center
)

        # ==================================================
        # Add Frames
        # ==================================================

        self.main.add(
            self.chat_frame,
            weight=1
        )

        self.main.add(
            self.center,
            weight=4
        )

        self.center.add(
            self.parameter_frame,
            weight=1
        )

        self.center.add(
            self.viewport_frame,
            weight=4
        )

        # ==================================================
        # Chat Panel
        # ==================================================

        self.chat_panel = ChatPanel(
            self.chat_frame
        )

        self.chat_panel.pack(
            fill="both",
            expand=True
        )

        # ==================================================
        # Parameter Panel
        # ==================================================

        self.parameter_panel = ParameterPanel(
            self.parameter_frame
        )

        self.parameter_panel.pack(
            fill="both",
            expand=True
        )
        ##################################################
# Viewport
##################################################

        self.viewport_panel = ViewportPanel(
        self.viewport_frame
)

        self.viewport_panel.pack(
        fill="both",
        expand=True
)

        # ==================================================
        # Temporary Sample Parameters
        # (Will be replaced by AI-generated parameters later)
        # ==================================================

        self.parameter_panel.load_parameters(
            {
                "Width": 120,
                "Height": 80,
                "Depth": 60,
                "Thickness": 3,
                "Radius": 10,
                "Fillet": 2,
                "Hole Diameter": 5,
                "Angle": 35
            }
        )
        self.parameter_panel.set_model_name("Phone Stand")

        # ==================================================
        # Status Bar
        # ==================================================
        ##################################################
# Event Registration
##################################################

        self.event_bus.subscribe(
    STATUS_CHANGED,
    self.update_status
)

        self.event_bus.subscribe(
    MODEL_GENERATED,
    self.on_model_generated
)
        self.status = StatusBar(self.root)
        self.status.set("Ready")
        self.event_bus.subscribe(
    TOOL_UNDO,
    lambda _: self.context.command_manager.undo()
)

        self.event_bus.subscribe(
    TOOL_REDO,
    lambda _: self.context.command_manager.redo()
)

        self.event_bus.subscribe(
    TOOL_NEW,
    self.on_new_project
)

        self.event_bus.subscribe(
    TOOL_SAVE,
    self.on_save_project
)

        self.event_bus.subscribe(
    TOOL_GENERATE,
    self.on_generate_model
)
    ######################################################
    ##################################################

    def update_status(self, text):
 
        self.status.set(text)

##################################################

    def on_model_generated(self, data):

        if not data:

            return

        design_state.set_model(

            data["name"],

            data["parameters"]

    )

        self.parameter_panel.set_model_name(

        design_state.model_name

    )

        self.parameter_panel.load_parameters(

        design_state.parameters

    )

        self.status.set(

        "Model Generated"
    )
    def show(self):
        self.root.mainloop()
    ##########################################################

    def on_new_project(self, _=None):

        self.context.design_state.reset()

        self.parameter_panel.clear_parameters()

        self.parameter_panel.set_model_name("No Model")

        self.status.set("New Project")

##########################################################

    def on_save_project(self, _=None):

        self.status.set("Save Project (Coming Soon)")

##########################################################

    def on_generate_model(self, _=None):

        self.status.set("Waiting for AI...")