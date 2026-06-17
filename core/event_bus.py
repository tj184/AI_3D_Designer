"""
Simple Event Bus

Allows every module to communicate without
depending on each other.

Chat -> AI
AI -> CAD
CAD -> Viewport
Viewport -> Status Bar

etc.
"""


class EventBus:

    def __init__(self):

        self.listeners = {}

    ##########################################################

    def subscribe(self, event_name, callback):

        if event_name not in self.listeners:

            self.listeners[event_name] = []

        self.listeners[event_name].append(callback)

    ##########################################################

    def unsubscribe(self, event_name, callback):

        if event_name not in self.listeners:

            return

        if callback in self.listeners[event_name]:

            self.listeners[event_name].remove(callback)

    ##########################################################

    def publish(self, event_name, data=None):

        callbacks = self.listeners.get(event_name, [])

        for callback in callbacks:

            callback(data)


event_bus = EventBus()