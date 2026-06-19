from core.cad.cad_generator import CADGenerator


class CADBuilder:

    def __init__(self, context):

        self.context = context

        self.generator = CADGenerator(context)

    ########################################################

    def build(self, data):

        self.context.logger.info("Kernel-based CAD build")

        try:
            self.context.parametric_kernel.set_base(
                data.get("parameters", {})
            )

            return self.context.parametric_kernel.rebuild()
        except ModuleNotFoundError as e:
            # CadQuery/OCP not available
            self.context.logger.warning(f"CAD build unavailable: {e}")
            # Return mock model data
            return {
                "name": data.get("name", "Model"),
                "parameters": data.get("parameters", {}),
                "type": "mock_model"
            }
        except Exception as e:
            self.context.logger.error(f"CAD build error: {e}")
            return None