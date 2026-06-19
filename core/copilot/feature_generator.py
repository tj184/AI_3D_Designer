class FeatureGenerator:

    def generate(self, intent):

        features = []

        obj = intent["object"]

        # -------------------------
        # PHONE HOLDER LOGIC
        # -------------------------

        if obj == "phone_holder":

            features.append({
                "type": "extrude",
                "params": {
                    "height": 120
                }
            })

            features.append({
                "type": "cut",
                "params": {
                    "w": 20,
                    "d": 10,
                    "h": 80
                }
            })

            features.append({
                "type": "hole",
                "params": {
                    "x": 0,
                    "y": 0,
                    "diameter": 6
                }
            })

        # -------------------------
        # BOX LOGIC
        # -------------------------

        elif obj == "container":

            features.append({
                "type": "extrude",
                "params": {
                    "height": 50
                }
            })

        return features