import ttkbootstrap as ttk


class StatusBar(ttk.Frame):

    def __init__(self, master):

        super().__init__(master)

        self.pack(fill="x", side="bottom")

        self.status = ttk.StringVar()

        self.status.set("Ready")

        ttk.Label(

            self,

            textvariable=self.status,

            anchor="w",

            padding=(10, 5)

        ).pack(fill="x")

    def set(self, text):

        self.status.set(text)