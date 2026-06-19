class LivePatchEngine:

    def __init__(self, context):

        self.context = context
        self.current_model = None

    ########################################################

    def apply(self, data):

        """
        Incrementally update CAD model
        """
        import cadquery as cq

        params = data.get("parameters", {})
        features = data.get("features", [])

        model = cq.Workplane("XY")

        # Base
        model = model.box(
            params.get("Width", 100),
            params.get("Depth", 100),
            params.get("Height", 20)
        )

        # Features applied progressively
        for f in features:

            ftype = f.get("type")

            if ftype == "hole":

                model = self._hole(model, f)

            elif ftype == "cut":

                model = self._cut(model, f)

        self.current_model = model

        return model

    ########################################################

    def _hole(self, model, f):

        p = f.get("params", {})

        return (
            model.faces(">Z")
            .workplane()
            .center(p.get("x", 0), p.get("y", 0))
            .hole(p.get("diameter", 5))
        )

    ########################################################

    def _cut(self, model, f):

        p = f.get("params", {})

        return model.cut(
            cq.Workplane("XY").box(
                p.get("w", 10),
                p.get("d", 10),
                p.get("h", 10)
            )
        )