from abc import ABC, abstractmethod

class Controller(ABC):
    @abstractmethod
    def process(self):
        """Define a lógica de controle entre sensores e atuadores"""
        pass
