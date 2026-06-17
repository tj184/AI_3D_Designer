import ttkbootstrap as ttk
from tkinter import scrolledtext


class ChatPanel(ttk.Frame):

    def __init__(self, master):

        super().__init__(master, padding=8)

        self.create_widgets()

    #######################################################

    def create_widgets(self):

        # ---------------- Header ---------------- #

        header = ttk.Frame(self)
        header.pack(fill="x")

        ttk.Label(
            header,
            text="AI Designer",
            font=("Segoe UI", 12, "bold")
        ).pack(side="left")

        ttk.Button(
            header,
            text="Clear"
        ).pack(side="right")

        # ---------------- Conversation ---------------- #

        self.chat_history = scrolledtext.ScrolledText(

            self,

            wrap="word",

            height=20,

            state="disabled"

        )

        self.chat_history.pack(

            fill="both",

            expand=True,

            pady=8

        )

        # ---------------- Prompt ---------------- #

        ttk.Label(

            self,

            text="Describe your design"

        ).pack(anchor="w")

        self.prompt = ttk.Text(

            self,

            height=5

        )

        self.prompt.pack(

            fill="x",

            pady=5

        )

        button_frame = ttk.Frame(self)

        button_frame.pack(fill="x")

        ttk.Button(

            button_frame,

            text="Generate"

        ).pack(

            side="left",

            padx=2

        )

        ttk.Button(

            button_frame,

            text="Stop"

        ).pack(

            side="left",

            padx=2

        )

        ttk.Button(

            button_frame,

            text="Regenerate"

        ).pack(

            side="left",

            padx=2

        )

    #######################################################

    def add_message(self, sender, message):

        self.chat_history.configure(state="normal")

        self.chat_history.insert(

            "end",

            f"{sender}:\n",

            "bold"

        )

        self.chat_history.insert(

            "end",

            message + "\n\n"

        )

        self.chat_history.tag_config(

            "bold",

            font=("Segoe UI", 10, "bold")

        )

        self.chat_history.configure(state="disabled")

        self.chat_history.see("end")