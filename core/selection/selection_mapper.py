class SelectionMapper:

    @staticmethod
    def map_to_parameter(data):

        """
        Convert selection → parameter update
        """

        if not data:
            return None

        # Example mapping logic
        # (Later extended for real BREP data)

        return {
            "parameter": "Width",
            "value": 150
        }