import os


class ExportService:

    def __init__(self, context):
        self.context = context

    ########################################################

    def export_stl(self, model, path="output/model.stl"):

        self._ensure_dir(path)

        self.context.logger.info("Exporting STL...")

        model.exportStl(path)

        return path

    ########################################################

    def export_step(self, model, path="output/model.step"):

        self._ensure_dir(path)

        self.context.logger.info("Exporting STEP...")

        model.exportStep(path)

        return path

    ########################################################

    def _ensure_dir(self, path):

        directory = os.path.dirname(path)

        if directory and not os.path.exists(directory):

            os.makedirs(directory)