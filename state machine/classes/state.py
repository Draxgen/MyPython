import atm
from abc import ABC

class State(ABC):
    @property
    def atm(self) -> ATM:
        pass
