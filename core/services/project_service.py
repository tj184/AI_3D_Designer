from core.constants import *


class ProjectService:

    def __init__(self, context):
        self.context = context
        self.event_bus = context.event_bus

        self.event_bus.subscribe(
            "PROJECT_SAVE",
            self.on_save_request
        )

    ########################################################

    def on_save_request(self, data=None):

        self.context.logger.info("Project Service: Save request received")

        self.context.task_manager.submit(
            "Project Save",
            self.save_project,
            data
        )

    ########################################################

    def save_project(self, data=None):

        self.context.logger.info("Saving project...")

        self.context.project_store.save()

        return True

    ########################################################

    def load_project(self, project_path):

        self.context.logger.info(f"Loading project: {project_path}")

        self.context.project_store.load()

        self.event_bus.publish(
            STATUS_CHANGED,
            "Project loaded"
        )

        return True
