from ui.main_window import MainWindow


class AI3DApplication:

    def __init__(self, root, context):

        self.context = context

        self.window = MainWindow(
            root=root,
            context=context
        )

    ##########################################################

    def run(self):

        self.window.show()

    ##########################################################

    def shutdown(self):

        self.context.shutdown()