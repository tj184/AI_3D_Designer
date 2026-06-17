"""
Command Manager

Provides Undo/Redo functionality for the application.

Each command consists of:
- execute()
- undo()

Example:

command = Command(
    name="Change Width",
    execute=lambda: ...,
    undo=lambda: ...
)

context.command_manager.execute(command)
"""

from dataclasses import dataclass
from typing import Callable, Optional

from core.event_bus import event_bus


# ==========================================================
# Command
# ==========================================================

@dataclass
class Command:

    name: str

    execute: Callable

    undo: Optional[Callable] = None


# ==========================================================
# Command Manager
# ==========================================================

class CommandManager:

    def __init__(self):

        self.undo_stack = []

        self.redo_stack = []

    ##########################################################

    def execute(self, command: Command):

        """
        Execute a command and store it
        for Undo.
        """

        command.execute()

        self.undo_stack.append(command)

        self.redo_stack.clear()

        event_bus.publish(
            "COMMAND_EXECUTED",
            command.name
        )

    ##########################################################

    def undo(self):

        if not self.undo_stack:
            return

        command = self.undo_stack.pop()

        if command.undo:
            command.undo()

        self.redo_stack.append(command)

        event_bus.publish(
            "COMMAND_UNDO",
            command.name
        )

    ##########################################################

    def redo(self):

        if not self.redo_stack:
            return

        command = self.redo_stack.pop()

        command.execute()

        self.undo_stack.append(command)

        event_bus.publish(
            "COMMAND_REDO",
            command.name
        )

    ##########################################################

    def clear(self):

        self.undo_stack.clear()

        self.redo_stack.clear()

    ##########################################################

    def can_undo(self):

        return len(self.undo_stack) > 0

    ##########################################################

    def can_redo(self):

        return len(self.redo_stack) > 0