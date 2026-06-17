import ttkbootstrap as ttk


class ViewportPanel(ttk.Frame):

    def __init__(self, master):

        super().__init__(master)

        self.create_widgets()

    #########################################################

    def create_widgets(self):

        ####################################################
        # Toolbar
        ####################################################

        toolbar = ttk.Frame(self)

        toolbar.pack(
            fill="x",
            padx=5,
            pady=5
        )

        buttons = [

            "🏠 Home",

            "Front",

            "Top",

            "Left",

            "Right",

            "Iso",

            "Wire",

            "Shaded",

            "Fit"

        ]

        for text in buttons:

            ttk.Button(
                toolbar,
                text=text,
                width=8
            ).pack(
                side="left",
                padx=2
            )

        ####################################################
        # Viewport
        ####################################################

        self.viewport = ttk.Frame(
            self,
            bootstyle="dark"
        )

        self.viewport.pack(
            fill="both",
            expand=True,
            padx=5,
            pady=5
        )

        ttk.Label(

            self.viewport,

            text="3D VIEWPORT\n\n(VTK Renderer will be loaded here)",

            font=("Segoe UI", 18, "bold"),

            anchor="center"

        ).place(

            relx=0.5,

            rely=0.5,

            anchor="center"

        )

        ####################################################
        # Bottom Status
        ####################################################

        bottom = ttk.Frame(self)

        bottom.pack(
            fill="x",
            padx=5,
            pady=5
        )

        ttk.Label(

            bottom,

            text="Coordinates : (0,0,0)"

        ).pack(side="left")

        ttk.Label(

            bottom,

            text="Camera : Perspective"

        ).pack(side="left", padx=20)

        ttk.Label(

            bottom,

            text="Status : Ready"

        ).pack(side="right")