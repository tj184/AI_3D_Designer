import ttkbootstrap as ttk
from tkinter import scrolledtext


class ChatPanel(ttk.Frame):

    def __init__(self, master, context=None, event_bus=None):

        super().__init__(master, padding=8)

        self.context = context
        self.event_bus = event_bus
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
            text="Clear",
            command=self.clear_chat
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

            text="Generate",
            command=self.on_generate

        ).pack(

            side="left",

            padx=2

        )

        ttk.Button(

            button_frame,

            text="Stop",
            command=self.on_stop

        ).pack(

            side="left",

            padx=2

        )

        ttk.Button(

            button_frame,

            text="Regenerate",
            command=self.on_regenerate

        ).pack(

            side="left",

            padx=2

        )

    #######################################################

    def on_generate(self):
        """Handle generate button click"""
        prompt_text = self.prompt.get("1.0", "end").strip()
        
        if not prompt_text:
            self.add_message("System", "Please enter a design description")
            return
        
        self.add_message("You", prompt_text)
        self.add_message("AI", "Generating design...")
        
        # Store prompt in design state
        if self.context:
            self.context.design_state.last_prompt = prompt_text
        
        # Publish generate event
        if self.event_bus:
            from core.constants import TOOL_GENERATE
            self.event_bus.publish(TOOL_GENERATE)
        
        # Clear prompt input
        self.prompt.delete("1.0", "end")

    #######################################################

    def on_stop(self):
        """Handle stop button click"""
        self.add_message("System", "Generation stopped")

    #######################################################

    def on_regenerate(self):
        """Handle regenerate button click"""
        if self.context and self.context.design_state.last_prompt:
            self.on_generate()
        else:
            self.add_message("System", "No previous prompt to regenerate")

    #######################################################

    def clear_chat(self):
        """Clear chat history"""
        self.chat_history.configure(state="normal")
        self.chat_history.delete("1.0", "end")
        self.chat_history.configure(state="disabled")

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