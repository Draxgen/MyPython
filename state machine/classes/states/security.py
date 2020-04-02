from ..state import State
from time import sleep
from .choose_operation import ChooseOperation

class Security(State):
    def handle1(self) -> None:
        print('Checking card ...')
        sleep(3)
        print("Card is correct")
        self.context.transition_to(ChooseOperation())