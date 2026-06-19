import os


class Settings:

    def __init__(self):

        # App Info
        self.APP_NAME = "AI CAD Studio"
        self.VERSION = "1.0"

        # Window
        self.WINDOW_WIDTH = 1400
        self.WINDOW_HEIGHT = 800

        # UI Layout
        self.CHAT_WIDTH = 300
        self.PARAMETER_WIDTH = 300
        self.MIN_WIDTH = 1200
        self.MIN_HEIGHT = 700

        # Paths
        self.PROJECT_DIR = os.path.join(os.getcwd(), "projects")
        self.EXPORT_DIR = os.path.join(os.getcwd(), "exports")
        self.LOG_DIR = os.path.join(os.getcwd(), "logs")

        # AI config
        self.OLLAMA_MODEL = "gemma4:31b-cloud"
        self.OLLAMA_URL = "http://localhost:11434"

        # CAD config
        self.DEFAULT_UNITS = "mm"


# GLOBAL INSTANCE (THIS FIXES YOUR ERROR)
settings = Settings()