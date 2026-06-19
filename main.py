import ttkbootstrap as ttk

from core.theme import create_window
from core.context import ApplicationContext

from ui.main_window import MainWindow


def main():

    # -----------------------------
    # Create Root Window
    # -----------------------------
    root = create_window()

    # -----------------------------
    # Initialize Global Context
    # -----------------------------
    context = ApplicationContext()

    # attach context globally
    context.initialize()

    # -----------------------------
    # Create UI
    # -----------------------------
    app = MainWindow(root, context)

    # -----------------------------
    # Start App
    # -----------------------------
    app.show()


if __name__ == "__main__":
    main()