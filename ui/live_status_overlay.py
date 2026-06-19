import ttkbootstrap as ttk


class LiveStatusOverlay(ttk.Frame):

    def __init__(self, master):

        super().__init__(master)

        self.label = ttk.Label(
            self,
            text="Idle",
            bootstyle="inverse"
        )

        self.label.pack(padx=10, pady=5)

    ########################################################

    def update_status(self, text):

        self.label.config(text=text)