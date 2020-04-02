from .atm import ATM
from abc import ABC, abstractmethod

class State(ABC):
    
    @property
    def context(self) -> ATM:
        return self._context
    
    @context.setter
    def context(self, context: ATM) -> None:
        self._context = context

    @abstractmethod
    def handle0(self) -> None:
        pass
    
    @abstractmethod
    def handle1(self) -> None:
        pass

    @abstractmethod
    def handle2(self) -> None:
        pass

    @abstractmethod
    def handle3(self) -> None:
        pass

    @abstractmethod
    def handle4(self) -> None:
        pass