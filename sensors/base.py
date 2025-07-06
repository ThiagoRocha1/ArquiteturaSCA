from abc import ABC, abstractmethod

class Sensor(ABC):
    @abstractmethod
    def read(self):
        """Deve retornar o valor atual lido pelo sensor"""
        pass
