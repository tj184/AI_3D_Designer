from core.constants import *
from core.context import context


class CADService:

    def __init__(self, context):

        self.context = context
        self.event_bus = context.event_bus

        self.event_bus.subscribe(
            MODEL_GENERATED,
            self.on_model_generated
        )

    ########################################################

    def on_model_generated(self, data):

        self.context.logger.info("CAD Service received model")

        self.context.task_manager.submit(
            "CAD Generation",
            self.build_model,
            data
        )

    ########################################################

    def build_model(self, data):

        # ------------------------------
        # Placeholder CAD execution
        # ------------------------------

        self.context.logger.info("Building CAD model...")

        import time
        time.sleep(2)

        self.context.design_state.stl_file = "output/model.stl"
        self.context.design_state.step_file = "output/model.step"

        self.event_bus.publish(
            STATUS_CHANGED,
            "CAD Model Generated"
        )

        return {
            "stl": self.context.design_state.stl_file,
            "step": self.context.design_state.step_file
        }