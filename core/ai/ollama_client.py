import requests
import json


class OllamaClient:

    def __init__(self, model="gemma4:e2b", host="http://localhost:11434"):
        self.model = model
        self.host = host

    ########################################################

    def generate(self, prompt):

        url = f"{self.host}/api/generate"

        payload = {
            "model": self.model,
            "prompt": prompt,
            "stream": False
        }

        response = requests.post(url, json=payload)

        if response.status_code != 200:
            raise Exception(f"Ollama Error: {response.text}")

        data = response.json()

        return data.get("response", "")