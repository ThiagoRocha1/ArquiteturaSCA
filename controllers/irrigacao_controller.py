from controllers.base import Controller

class IrrigationController(Controller):
    def __init__(self, sensors, actuators, min_moisture=30.0):
        self.sensors = sensors
        self.actuators = actuators
        self.min_moisture = min_moisture

    def process(self):
        for sensor in self.sensors:
            moisture = sensor.read()
            print(f"🌱 Umidade do solo: {moisture}%")
            action = "abrir" if moisture < self.min_moisture else "fechar"
            for actuator in self.actuators:
                actuator.act(action)
