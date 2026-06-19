import json


class SafeJSON:

    @staticmethod
    def loads(text):

        try:
            return json.loads(text)

        except Exception:

            # fallback extraction
            start = text.find("{")
            end = text.rfind("}")

            if start == -1 or end == -1:
                return None

            try:
                return json.loads(text[start:end+1])
            except:
                return None

    ########################################################

    @staticmethod
    def dumps(data):

        return json.dumps(data, indent=2)