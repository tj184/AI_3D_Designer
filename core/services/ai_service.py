import json
from core.constants import *
from core.context import context


class AIService:

    def __init__(self, context):
        self.context = context
        self.event_bus = context.event_bus

        # Listen for generate requests
        self.event_bus.subscribe(
            TOOL_GENERATE,
            self.on_generate_request
        )

    ########################################################

    def on_generate_request(self, _=None):

        self.context.logger.info("AI Service: Generate request received")

        prompt = self._get_last_prompt()

        if not prompt:
            self.context.logger.info("No prompt found")
            return

        self.context.task_manager.submit(
            "AI Generation",
            self.generate_model,
            prompt
        )

    ########################################################

    def _get_last_prompt(self):

        # Temporary placeholder (chat integration later)
        return getattr(self.context.design_state, "last_prompt", None)

    ########################################################

    def generate_model(self, prompt):

        # ------------------------------
        # MOCK AI (replace with Ollama later)
        # ------------------------------

        self.context.logger.info(f"Generating model for: {prompt}")

        # Fake AI output
        result = {
            "name": "AI_Model",
            "parameters": {
                "Width": 120,
                "Height": 80,
                "Depth": 60,
                "Radius": 10,
                "Angle": 35
            },
            "cad_code": "# CadQuery code placeholder"
        }

        # Store in state
        self.context.design_state.set_model(
            result["name"],
            result["parameters"]
        )

        self.context.design_state.cad_code = result["cad_code"]

        # Notify system
        self.event_bus.publish(
            MODEL_GENERATED,
            result
        )

        return result