from core.constants import *
from core.parametric.debouncer import Debouncer
from core.parametric.cache import ModelCache


class ParametricRegenerator:

    def __init__(self, context):

        self.context = context
        self.event_bus = context.event_bus

        self.debouncer = Debouncer(0.4)
        self.cache = ModelCache()

        self.bind_events()

    ########################################################

    def bind_events(self):

        self.event_bus.subscribe(
            "PARAMETER_CHANGED",
            self.on_parameter_changed
        )

    ########################################################

    def on_parameter_changed(self, data):

        self.context.logger.info("Parameter changed → scheduling regen")

        self.debouncer.call(
            self.regenerate
        )

    ########################################################

    def regenerate(self):

        params = self.context.design_state.parameters

        # -----------------------------
        # CACHE CHECK
        # -----------------------------

        cached = self.cache.get(params)

        if cached:

            self.context.logger.info("Using cached model")

            self.context.design_state.stl_file = cached

            self.event_bus.publish(
                MODEL_GENERATED,
                {"cached": True}
            )

            return

        # -----------------------------
        # REBUILD PIPELINE
        # -----------------------------

        self.context.logger.info("Regenerating CAD model")

        def task():

            model = self.context.cad_builder.build({
                "name": self.context.design_state.model_name,
                "parameters": params,
                "features": []
            })

            stl_path = self.context.export_service.export_stl(model)

            self.context.design_state.stl_file = stl_path

            self.cache.set(params, stl_path)

            self.event_bus.publish(
                MODEL_GENERATED,
                {"regenerated": True}
            )

        self.context.task_manager.submit(
            "Parametric Regen",
            task
        )