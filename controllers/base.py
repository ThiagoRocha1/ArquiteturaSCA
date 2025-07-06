from abc import ABC, abstractmethod

class Controller(ABC):
    @abstractmethod
    def process(self) -> None:
        """Define a lógica de controle entre sensores e atuadores"""
        pass
