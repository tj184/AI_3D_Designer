from dataclasses import dataclass, field


@dataclass
class DesignState:

    ####################################################

    project_name: str = "Untitled"

    model_name: str = ""

    description: str = ""

    ####################################################

    parameters: dict = field(default_factory=dict)

    ####################################################

    cad_code: str = ""

    ####################################################

    stl_file: str = ""

    step_file: str = ""

    ####################################################

    chat_history: list = field(default_factory=list)

    ####################################################

    modified: bool = False

    ####################################################

    def reset(self):

        self.model_name = ""

        self.description = ""

        self.parameters.clear()

        self.cad_code = ""

        self.stl_file = ""

        self.step_file = ""

        self.chat_history.clear()

        self.modified = False

    ####################################################

    def update_parameter(self, name, value):

        self.parameters[name] = value

        self.modified = True

    ####################################################

    def set_model(self, name, parameters):

        self.model_name = name

        self.parameters = parameters

        self.modified = True


design_state = DesignState()