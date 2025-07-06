class IoTThing:
    def __init__(self, controller):
        self.controller = controller

    def run(self, interval=2, cycles=10):
        import time
        for _ in range(cycles):
            self.controller.process()
            time.sleep(interval)
