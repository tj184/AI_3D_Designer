import os


class FileUtils:

    @staticmethod
    def ensure_dir(path):

        folder = os.path.dirname(path)

        if folder and not os.path.exists(folder):
            os.makedirs(folder)

    ########################################################

    @staticmethod
    def exists(path):
        return os.path.exists(path)

    ########################################################

    @staticmethod
    def safe_write(path, data, mode="w"):

        FileUtils.ensure_dir(path)

        with open(path, mode) as f:
            f.write(data)

    ########################################################

    @staticmethod
    def safe_read(path):

        if not FileUtils.exists(path):
            return None

        with open(path, "r") as f:
            return f.read()