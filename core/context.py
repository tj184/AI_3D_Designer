"""
Application Context

The ApplicationContext is the central object shared across the
entire application.

Instead of passing many objects to every class, we pass only
the context.

Example:

context.event_bus.publish(...)
context.design_state.parameters
context.task_manager.submit(...)
"""

from core.event_bus import event_bus
from core.logger import logger
from core.settings import settings
from models.design_state import design_state
from core.task_manager import TaskManager
from core.command import CommandManager
from core.services.ai_service import AIService
from core.services.cad_service import CADService
from core.services.project_service import ProjectService


class ApplicationContext:
    """
    Central application context.

    Stores all global services and shared state.
    """

    def __init__(self):

        # -------------------------------------------------
        # Core Services
        # -------------------------------------------------

        self.event_bus = event_bus

        self.logger = logger

        self.settings = settings

        self.design_state = design_state

        # -------------------------------------------------
        # Runtime Services
        # (Initialized later)
        # -------------------------------------------------

        self.task_manager = None

        self.command_manager = CommandManager()

        self.ai_service = None

        self.cad_service = None

        self.project_service = None

        self.export_service = None

        # -------------------------------------------------
        # Runtime Flags
        # -------------------------------------------------

        self.running = False

    ########################################################

    def initialize(self):
        """
        Called once when the application starts.
        """

        self.running = True

        self.task_manager = TaskManager()

        self.logger.info("Task Manager Created")

        self.logger.info("Application Context Initialized")
        # Services
        self.ai_service = AIService(self)
        self.cad_service = CADService(self)
        self.project_service = ProjectService(self)

        self.logger.info("Services Initialized")

    ########################################################

    def shutdown(self):
        """
        Called before closing the application.
        """

        self.running = False

        if self.task_manager:

            self.task_manager.shutdown()

        self.logger.info("Application Context Shutdown")

    ########################################################

    def set_task_manager(self, manager):

        self.task_manager = manager

    ########################################################

  

    ########################################################

    def set_ai_service(self, service):

        self.ai_service = service

    ########################################################

    def set_cad_service(self, service):

        self.cad_service = service

    ########################################################

    def set_project_service(self, service):

        self.project_service = service

    ########################################################

    def set_export_service(self, service):

        self.export_service = service


# ----------------------------------------------------------
# Singleton Context
# ----------------------------------------------------------

context = ApplicationContext()