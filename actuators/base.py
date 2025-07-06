from abc import ABC, abstractmethod

class Actuator(ABC):
    @abstractmethod
    def act(self, command: str) -> None:
        """Executar uma ação baseado em um comando"""
        pass