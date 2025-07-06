import time
from controllers.base import Controller

class IoTThing:
    def __init__(self, controller: Controller) -> None:
        self._controller = controller 

    def run(self, interval: int = 2, cycles: int = 10) -> None:
        for _ in range(cycles):
            self._controller.process()
            time.sleep(interval)