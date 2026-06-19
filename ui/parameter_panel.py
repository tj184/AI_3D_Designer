import ttkbootstrap as ttk


class ParameterPanel(ttk.Frame):

    def __init__(self, master):

        super().__init__(master, padding=8)

        self.variables = {}
        self.entries = {}

        self.create_layout()

    #########################################################
    # Layout
    #########################################################

    def create_layout(self):

        # =====================================================
        # Title
        # =====================================================

        ttk.Label(
            self,
            text="Model Properties",
            font=("Segoe UI", 13, "bold")
        ).pack(anchor="w", pady=(0, 10))

        # =====================================================
        # Model Information
        # =====================================================

        info_frame = ttk.Labelframe(
            self,
            text="Model Information",
            padding=8
        )

        info_frame.pack(fill="x", pady=(0, 10))

        self.model_name = ttk.StringVar(value="No Model")

        ttk.Label(
            info_frame,
            text="Object:"
        ).grid(row=0, column=0, sticky="w")

        ttk.Label(
            info_frame,
            textvariable=self.model_name,
            bootstyle="info"
        ).grid(row=0, column=1, sticky="w", padx=5)

        # =====================================================
        # Parameters
        # =====================================================

        parameter_frame = ttk.Labelframe(
            self,
            text="Parameters",
            padding=5
        )

        parameter_frame.pack(
            fill="both",
            expand=True
        )

        self.canvas = ttk.Canvas(parameter_frame)

        scrollbar = ttk.Scrollbar(
            parameter_frame,
            orient="vertical",
            command=self.canvas.yview
        )

        self.scroll_frame = ttk.Frame(self.canvas)

        self.scroll_frame.bind(
            "<Configure>",
            lambda e: self.canvas.configure(
                scrollregion=self.canvas.bbox("all")
            )
        )

        self.canvas.create_window(
            (0, 0),
            window=self.scroll_frame,
            anchor="nw"
        )

        self.canvas.configure(
            yscrollcommand=scrollbar.set
        )

        self.canvas.pack(
            side="left",
            fill="both",
            expand=True
        )

        scrollbar.pack(
            side="right",
            fill="y"
        )

        # =====================================================
        # Project Actions
        # =====================================================

        actions = ttk.Labelframe(
            self,
            text="Project Actions",
            padding=8
        )

        actions.pack(fill="x", pady=10)

        ttk.Button(
            actions,
            text="Apply Changes"
        ).pack(fill="x", pady=2)

        ttk.Button(
            actions,
            text="Reset Parameters"
        ).pack(fill="x", pady=2)

        ttk.Button(
            actions,
            text="Regenerate AI Model"
        ).pack(fill="x", pady=2)

        ttk.Separator(actions).pack(fill="x", pady=8)

        ttk.Button(
            actions,
            text="Save Project"
        ).pack(fill="x", pady=2)

        ttk.Button(
            actions,
            text="Export STL"
        ).pack(fill="x", pady=2)

        ttk.Button(
            actions,
            text="Export STEP"
        ).pack(fill="x", pady=2)

    #########################################################
    # Remove Existing Parameters
    #########################################################

    def clear_parameters(self):

        for widget in self.scroll_frame.winfo_children():
            widget.destroy()

        self.variables.clear()
        self.entries.clear()

    #########################################################
    # Load Parameters
    #########################################################

    def load_parameters(self, params):

        """
        Example:

        params = {
            "Width":120,
            "Height":80,
            "Depth":60,
            "Radius":5,
            "Angle":45
        }
        """

        self.clear_parameters()

        for name, value in params.items():

            row = ttk.Frame(self.scroll_frame)

            row.pack(
                fill="x",
                pady=4
            )

            ttk.Label(
                row,
                text=name,
                width=15
            ).pack(side="left")

            var = ttk.DoubleVar(value=value)

            entry = ttk.Entry(
                row,
                textvariable=var,
                width=10
            )

            entry.pack(
                side="left",
                padx=5
            )

            # Display units
            unit = "°" if "angle" in name.lower() else "mm"

            ttk.Label(
                row,
                text=unit,
                foreground="gray"
            ).pack(side="left")

            self.variables[name] = var
            self.entries[name] = entry

    #########################################################
    # Update Model Name
    #########################################################

    def set_model_name(self, name):

        self.model_name.set(name)

    #########################################################
    # Get Parameters
    #########################################################

    def get_parameters(self):

        data = {}

        for key, var in self.variables.items():

            data[key] = var.get()

        return data
    def bind_selection(self, context):

        self.context = context

        self.event_bus = context.event_bus

        self.event_bus.subscribe(
        "SELECTION_CHANGED",
        self.on_selection_changed
    )


    def on_selection_changed(self, data):

        if not data:
            return

    # Example auto-load
        params = self.context.design_state.parameters

        self.load_parameters(params)
    def bind_live_updates(self):

        for name, entry in self.entries.items():

            entry.bind(
            "<KeyRelease>",
            lambda e, n=name: self.on_change(n)
        )


    def on_change(self, name):

        value = self.variables[name].get()

        self.context.design_state.update_parameter(name, value)
    def live_update(self, name, value):

        self.context.design_state.update_parameter(name, value)

        self.context.event_bus.publish(
        "PARAMETER_CHANGED",
        {
            "name": name,
            "value": value,
            "live": True
        }
    )