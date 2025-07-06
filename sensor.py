import random

class Sensor:
    def read(self):
        raise NotImplementedError

class TemperatureSensor(Sensor):
    def read(self):
        """Simula leitura de temperatura ambiente"""
        return round(random.uniform(20.0, 35.0), 1)
