import json


class StreamJSONBuilder:

    def __init__(self):

        self.buffer = ""

    ########################################################

    def add_token(self, token):

        self.buffer += token

    ########################################################

    def try_parse(self):

        """
        Try extracting valid JSON from partial stream
        """

        try:

            start = self.buffer.find("{")
            end = self.buffer.rfind("}")

            if start == -1 or end == -1:
                return None

            candidate = self.buffer[start:end+1]

            return json.loads(candidate)

        except:
            return None

    ########################################################

    def reset(self):

        self.buffer = ""