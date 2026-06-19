class SelectionManager:

    def __init__(self, context):

        self.context = context
        self.selected_actor = None
        self.selected_data = None

    ########################################################

    def set_selection(self, actor, data=None):

        self.clear_selection()

        self.selected_actor = actor
        self.selected_data = data

        if actor:

            actor.GetProperty().SetColor(1.0, 0.6, 0.2)

        self.context.event_bus.publish(
            "SELECTION_CHANGED",
            data
        )

    ########################################################

    def clear_selection(self):

        if self.selected_actor:

            self.selected_actor.GetProperty().SetColor(0.8, 0.8, 0.9)

        self.selected_actor = None
        self.selected_data = None