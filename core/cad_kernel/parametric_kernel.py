from core.cad_kernel.feature_tree import FeatureTree
from core.cad_kernel.constraints import ConstraintSolver


class ParametricKernel:

    def __init__(self, context):

        self.context = context

        self.feature_tree = FeatureTree()
        self.solver = ConstraintSolver()

        self.base_params = {
            "Width": 100,
            "Depth": 100,
            "Height": 20
        }

    ########################################################

    def set_base(self, params):

        self.base_params.update(params)

    ########################################################

    def add_feature(self, feature):

        self.feature_tree.add(feature)

    ########################################################

    def rebuild(self):

        import cadquery as cq

        self.context.logger.info("Parametric Kernel rebuild")

        model = cq.Workplane("XY").box(
            self.base_params["Width"],
            self.base_params["Depth"],
            self.base_params["Height"]
        )

        model = self.feature_tree.rebuild(model)

        return model

    ########################################################

    def build_from_design_state(self):

        return self.rebuild()