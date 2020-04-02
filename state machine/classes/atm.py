from .state import State
from abc import ABC

class ATM(ABC):
    _state = None

    def __init__(self, state: State) -> None:
        self.transition_to(state)
    
    def transition_to(self, state:State):
        # change state
        self._state = state
        self._state.context = self

    def request0(self):
        self._state.handle0()
    
    def request1(self):
        self._state.handle1()

    def request2(self):
        self._state.handle2()

    def request3(self):
        self._state.handle3()

    def request4(self):
        self._state.handle4()