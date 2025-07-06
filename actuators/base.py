from abc import ABC, abstractmethod

class Actuator(ABC):
    @abstractmethod
    def act(self, command):
        """Deve executar uma ação baseada em um comando"""
        pass
