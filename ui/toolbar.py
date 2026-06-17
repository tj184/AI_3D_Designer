import ttkbootstrap as ttk

from core.constants import *


class Toolbar(ttk.Frame):

    def __init__(self, master, context):

        super().__init__(master)

        self.context = context
        self.event_bus = context.event_bus

        self.pack(
            fill="x",
            padx=2,
            pady=2
        )

        self.create_toolbar()

    ##########################################################

    def create_toolbar(self):

        toolbar = ttk.Frame(self)
        toolbar.pack(fill="x")

        # ---------------------------------------------------
        # Project
        # ---------------------------------------------------

        self.create_button("📄 New", TOOL_NEW)
        self.create_button("📂 Open", TOOL_OPEN)
        self.create_button("💾 Save", TOOL_SAVE)

        ttk.Separator(
            toolbar,
            orient="vertical"
        ).pack(side="left", fill="y", padx=5)

        # ---------------------------------------------------
        # Edit
        # ---------------------------------------------------

        self.create_button("↶ Undo", TOOL_UNDO)
        self.create_button("↷ Redo", TOOL_REDO)

        ttk.Separator(
            toolbar,
            orient="vertical"
        ).pack(side="left", fill="y", padx=5)

        # ---------------------------------------------------
        # AI
        # ---------------------------------------------------

        self.create_button("🤖 Generate", TOOL_GENERATE)

        ttk.Separator(
            toolbar,
            orient="vertical"
        ).pack(side="left", fill="y", padx=5)

        # ---------------------------------------------------
        # Export
        # ---------------------------------------------------

        self.create_button("STL", TOOL_EXPORT_STL)
        self.create_button("STEP", TOOL_EXPORT_STEP)

        ttk.Separator(
            toolbar,
            orient="vertical"
        ).pack(side="left", fill="y", padx=5)

        # ---------------------------------------------------
        # Settings
        # ---------------------------------------------------

        self.create_button("⚙ Settings", TOOL_SETTINGS)

    ##########################################################

    def create_button(self, text, event_name):

        ttk.Button(
            self,
            text=text,
            width=12,
            command=lambda: self.publish(event_name)
        ).pack(
            side="left",
            padx=2,
            pady=2
        )

    ##########################################################

    def publish(self, event_name):

        self.context.logger.info(f"Toolbar -> {event_name}")

        self.event_bus.publish(event_name)