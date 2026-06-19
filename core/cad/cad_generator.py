class CADGenerator:

    def __init__(self, context):
        self.context = context

    ########################################################

    def generate(self, data):
        """
        Convert AI JSON → CadQuery model (or mock if CadQuery unavailable)
        """
        try:
            import cadquery as cq
            return self._generate_with_cadquery(data)
        except ImportError:
            return self._generate_mock_model(data)

    ########################################################

    def _generate_with_cadquery(self, data):
        import cadquery as cq

        name = data.get("name", "Model")
        params = data.get("parameters", {})
        features = data.get("features", [])

        self.context.logger.info(f"Generating CAD: {name}")

        model = cq.Workplane("XY")

        # Base extrusion (default block)
        width = params.get("Width", 100)
        depth = params.get("Depth", 100)
        height = params.get("Height", 20)

        model = model.box(width, depth, height)

        # Apply features
        for feature in features:
            ftype = feature.get("type")
            
            if ftype == "hole":
                params_f = feature.get("params", {})
                diameter = params_f.get("diameter", 5)
                model = model.hole(diameter)
            
            elif ftype == "cut":
                params_f = feature.get("params", {})
                model = model.cut(
                    cq.Workplane("XY").box(
                        params_f.get("w", 20),
                        params_f.get("d", 10),
                        params_f.get("h", 80)
                    )
                )

        self.context.logger.info("CAD model generated successfully")
        return model

    ########################################################

    def _generate_mock_model(self, data):
        """Fallback mock model when CadQuery is unavailable"""
        name = data.get("name", "Model")
        params = data.get("parameters", {})
        
        self.context.logger.info(f"Generating mock CAD: {name}")
        
        # Return a simple dict representation
        return {
            "name": name,
            "parameters": params,
            "type": "mock_model",
            "dimensions": {
                "width": params.get("Width", 100),
                "depth": params.get("Depth", 100),
                "height": params.get("Height", 20)
            }
        }

        self.context.logger.info(f"Generating CAD: {name}")

        model = cq.Workplane("XY")

        # --------------------------------------------
        # Base extrusion (default block)
        # --------------------------------------------

        width = params.get("Width", 100)
        depth = params.get("Depth", 100)
        height = params.get("Height", 20)

        model = (
            model
            .box(width, depth, height)
        )

        # --------------------------------------------
        # Feature processing
        # --------------------------------------------

        for feature in features:

            ftype = feature.get("type")
            fparams = feature.get("params", {})

            if ftype == "hole":
                model = self._add_hole(model, fparams)

            elif ftype == "cut":
                model = self._add_cut(model, fparams)

            elif ftype == "fillet":
                model = self._add_fillet(model, fparams)

        return model

    ########################################################

    def _add_hole(self, model, params):

        diameter = params.get("diameter", 5)
        x = params.get("x", 0)
        y = params.get("y", 0)

        return (
            model.faces(">Z")
            .workplane()
            .center(x, y)
            .hole(diameter)
        )

    ########################################################

    def _add_cut(self, model, params):

        w = params.get("width", 10)
        d = params.get("depth", 10)
        h = params.get("height", 10)

        return model.cut(
            cq.Workplane("XY").box(w, d, h)
        )

    ########################################################

    def _add_fillet(self, model, params):

        radius = params.get("radius", 2)

        try:
            return model.edges().fillet(radius)
        except:
            return model