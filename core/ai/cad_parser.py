import json
from core.utils.safe_json import SafeJSON


class CADParser:

    def __init__(self, context=None):

        self.context = context

    ########################################################

    def parse(self, raw_output):

        """
        Converts AI output → structured CAD format
        """

        if not raw_output:
            return self._empty()

        # -----------------------------
        # STEP 1: SAFE JSON PARSE
        # -----------------------------
        data = SafeJSON.loads(raw_output)

        if not data:
            if self.context:
                self.context.logger.warning("CADParser: Invalid JSON, using fallback")
            return self._fallback()

        # -----------------------------
        # STEP 2: NORMALIZE STRUCTURE
        # -----------------------------
        return self._normalize(data)

    ########################################################

    def _normalize(self, data):

        """
        Ensures consistent CAD schema
        """

        return {
            "name": data.get("name", "AI_Model"),

            "parameters": self._safe_params(
                data.get("parameters", {})
            ),

            "features": self._safe_features(
                data.get("features", [])
            ),

            "metadata": {
                "source": "ai",
                "version": "1.0"
            }
        }

    ########################################################

    def _safe_params(self, params):

        if not isinstance(params, dict):
            return {}

        cleaned = {}

        for k, v in params.items():
            try:
                cleaned[k] = float(v)
            except:
                cleaned[k] = v

        return cleaned

    ########################################################

    def _safe_features(self, features):

        """
        Ensures feature tree is valid
        """

        if not isinstance(features, list):
            return []

        cleaned = []

        for f in features:

            if not isinstance(f, dict):
                continue

            feature_type = f.get("type")

            if not feature_type:
                continue

            cleaned.append({
                "type": feature_type,
                "params": f.get("params", {}),
                "name": f.get("name", feature_type)
            })

        return cleaned

    ########################################################

    def _fallback(self):

        """
        Safe fallback CAD model if AI fails
        """

        return {
            "name": "Fallback_Model",
            "parameters": {
                "Width": 100,
                "Depth": 100,
                "Height": 20
            },
            "features": [],
            "metadata": {
                "source": "fallback"
            }
        }

    ########################################################

    def _empty(self):

        return {
            "name": "Empty_Model",
            "parameters": {},
            "features": [],
            "metadata": {
                "source": "empty"
            }
        }