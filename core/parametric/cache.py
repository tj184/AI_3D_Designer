import hashlib
import json


class ModelCache:

    def __init__(self):

        self.cache = {}

    ########################################################

    def _hash(self, params):

        return hashlib.md5(
            json.dumps(params, sort_keys=True).encode()
        ).hexdigest()

    ########################################################

    def get(self, params):

        key = self._hash(params)

        return self.cache.get(key)

    ########################################################

    def set(self, params, model_path):

        key = self._hash(params)

        self.cache[key] = model_path