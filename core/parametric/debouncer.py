import time
import threading


class Debouncer:

    def __init__(self, delay=0.5):

        self.delay = delay
        self.timer = None

    ########################################################

    def call(self, func, *args, **kwargs):

        if self.timer:
            self.timer.cancel()

        self.timer = threading.Timer(
            self.delay,
            func,
            args=args,
            kwargs=kwargs
        )

        self.timer.start()