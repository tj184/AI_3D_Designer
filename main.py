from core.theme import create_window
from core.context import context
from core.app import AI3DApplication


def main():

    # ---------------------------------------------
    # Initialize application services
    # ---------------------------------------------

    context.initialize()

    # ---------------------------------------------
    # Create main window
    # ---------------------------------------------

    root = create_window()

    # ---------------------------------------------
    # Create application
    # ---------------------------------------------

    app = AI3DApplication(
        root=root,
        context=context
    )

    # ---------------------------------------------
    # Graceful shutdown
    # ---------------------------------------------

    def on_close():

        app.shutdown()

        root.destroy()

    root.protocol(
        "WM_DELETE_WINDOW",
        on_close
    )

    # ---------------------------------------------
    # Start UI
    # ---------------------------------------------

    app.run()


if __name__ == "__main__":

    main()