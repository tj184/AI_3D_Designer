from core.constants import *
from core.cad.geometry_validator import GeometryValidator


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

        self.context.logger.info("CAD Service building model...")

        self.context.task_manager.submit(
            "CAD Build",
            self.build_model,
            data
        )

    ########################################################

    def build_model(self, data):

        model = self.context.cad_builder.build(data)

        if not GeometryValidator.validate(model):

            self.context.logger.error("Invalid geometry")

            self.event_bus.publish(
                STATUS_CHANGED,
                "Invalid Model Geometry"
            )

            return None

        # Export (temporary auto-export)
        stl = self.context.export_service.export_stl(model)

        step = self.context.export_service.export_step(model)

        self.context.design_state.stl_file = stl
        self.context.design_state.step_file = step

        self.event_bus.publish(
            STATUS_CHANGED,
            "CAD Model Generated Successfully"
        )

        return {
            "stl": stl,
            "step": step
        }