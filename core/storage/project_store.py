import json
from core.utils.file_utils import FileUtils


class ProjectStore:

    def __init__(self, context):

        self.context = context

        self.project_file = "projects/current_project.ai3d"

    ########################################################

    def save(self):

        state = self.context.design_state

        data = {
            "name": state.model_name,
            "parameters": state.parameters,
            "cad_code": state.cad_code,
            "stl": state.stl_file,
            "step": state.step_file
        }

        FileUtils.safe_write(
            self.project_file,
            json.dumps(data, indent=2)
        )

        self.context.logger.info("Project saved")

        self.context.event_bus.publish(
            "STATUS_CHANGED",
            "Project Saved"
        )

    ########################################################

    def load(self):

        raw = FileUtils.safe_read(self.project_file)

        if not raw:
            self.context.logger.warning("No project found")
            return

        data = json.loads(raw)

        self.context.design_state.set_model(
            data.get("name", "Model"),
            data.get("parameters", {})
        )

        self.context.design_state.cad_code = data.get("cad_code")

        self.context.design_state.stl_file = data.get("stl")
        self.context.design_state.step_file = data.get("step")

        self.context.logger.info("Project loaded")

        self.context.event_bus.publish(
            "MODEL_GENERATED",
            data
        )