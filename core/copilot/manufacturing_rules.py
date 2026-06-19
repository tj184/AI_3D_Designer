class ManufacturingRules:

    def validate(self, features, intent):

        warnings = []

        for f in features:

            if f["type"] == "hole":

                if f["params"].get("diameter", 0) < 1:
                    warnings.append("Hole too small for printing")

            if f["type"] == "extrude":

                if f["params"].get("height", 0) > 200:
                    warnings.append("Model too tall for FDM printing")

        # global rules

        if intent["object"] == "phone_holder":

            warnings.append("Check angle stability for phone weight")

        return warnings