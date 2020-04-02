from ..state import State
from .security import Security
from time import sleep

class Idle(State):
    def handle0(self) -> None:
        print('Card inserted. Press 1')
        self.context.transition_to(Security())