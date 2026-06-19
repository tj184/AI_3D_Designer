class ErrorAnalyzer:

    @staticmethod
    def analyze(exception, params):

        """
        Convert CAD failure into structured AI feedback
        """

        return {
            "error_type": type(exception).__name__,
            "message": str(exception),
            "parameters": params,
            "suggestion": ErrorAnalyzer._suggest_fix(exception)
        }

    ########################################################

    @staticmethod
    def _suggest_fix(exception):

        msg = str(exception).lower()

        if "face" in msg:
            return "invalid geometry faces detected"

        if "volume" in msg:
            return "model is non-manifold or zero volume"

        if "fillet" in msg:
            return "reduce fillet radius"

        return "general cad construction failure"