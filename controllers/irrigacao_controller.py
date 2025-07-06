from typing import List
from actuators.base import Actuator
from controllers.base import Controller
from sensors.base import Sensor

class IrrigationController(Controller):
    def __init__(self, sensors: List[Sensor], actuators: List[Actuator], min_moisture: float = 30.0) -> None:
        self._sensors = sensors
        self._actuators = actuators
        self._min_moisture = min_moisture

    def process(self) -> None:
        for sensor in self._sensors:
            moisture = sensor.read()
            print(f"🌱 Umidade do solo: {moisture}%")
            action = "abrir" if moisture < self._min_moisture else "fechar"
            for actuator in self._actuators:
                actuator.act(action)
