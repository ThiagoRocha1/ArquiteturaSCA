import random
from sensors.base import Sensor

class SoilMoistureSensor(Sensor):
    def read(self):
        return round(random.uniform(10.0, 80.0), 1)
