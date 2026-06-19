import requests
import json


class StreamingOllama:

    def __init__(self, model="gemma4:e2b", host="http://localhost:11434"):
        self.model = model
        self.host = host

    ########################################################

    def stream(self, prompt):
        """
        Yields tokens from Ollama streaming API
        """

        url = f"{self.host}/api/generate"

        payload = {
            "model": self.model,
            "prompt": prompt,
            "stream": True
        }

        with requests.post(url, json=payload, stream=True) as response:

            for line in response.iter_lines():

                if not line:
                    continue

                data = json.loads(line.decode("utf-8"))

                yield data.get("response", "")