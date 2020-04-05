from __future__ import annotations
from abc import ABC, abstractmethod
from time import sleep
from msvcrt import getch

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

class ChooseOperation(State):

    def __init__(self):
        self.printmenu()

    @staticmethod
    def printmenu():
        print('Choose operation:')
        print('1 - Withdrawal')
        print('2 - Deposit')
        print('3 - Change PIN')
        print('4 - Exit')

    def handle0(self) -> None:
        pass

    def handle1(self) -> None:
        print('Withdrawal has been chosen')
        print('haha money printer go brrrr')

    def handle2(self) -> None:
        print('Deposit has been chosen')
        print('Give me yo money, bitch!')

    def handle3(self) -> None:
        print('Change PIN has been chosen')
        print('There. I\'vechanged your PIN. Good luck guessing it ;p')

    def handle4(self) -> None:
        print('Bye bye')
        self._context.transition_to(Cleanup())

class Cleanup(State):
    def __init__(self):
        print('Removing card... please take your card...')
        sleep(2)
        self.context.transition_to(Idle)

    def handle0(self) -> None:
        pass

    def handle1(self) -> None:
        pass

    def handle2(self) -> None:
        pass

    def handle3(self) -> None:
        pass

    def handle4(self) -> None:
        pass

class Idle(State):
    def __init__(self):
        print('Hello, welcome to this ATM!')
        print('Insert card to begin (Press 0)')

    def handle0(self) -> None:
        print('Card inserted. Please wait')
        self.context.transition_to(Security())

    def handle1(self) -> None:
        pass

    def handle2(self) -> None:
        pass

    def handle3(self) -> None:
        pass

    def handle4(self) -> None:
        pass

class MakeOperation(State):
    def __init__(self):
        print('Choose an operation')

    def handle0(self) -> None:
        pass

    def handle1(self) -> None:
        pass

    def handle2(self) -> None:
        pass

    def handle3(self) -> None:
        pass

    def handle4(self) -> None:
        pass

class Security(State):

    def __init__(self):
        print('Checking card ...')
        sleep(3)
        print("Card is correct")
        # todo: the transition_to function does not work in init. Look up and understand property setters. Understand the context variable
        self.context.transition_to(ChooseOperation())
    
    def handle1(self) -> None:
        pass

    def handle0(self) -> None:
        pass

    def handle2(self) -> None:
        pass

    def handle3(self) -> None:
        pass

    def handle4(self) -> None:
        pass

if __name__=='__main__':
    context = ATM(Idle())

    while True:
        
        input = str(getch())[2]
        
        if input == 'x':
            break
        
        try:
            exec(f'context.request{input}()')
            #print(input)
            #print(type(input))
        except:
            raise Exception('Something went wrong')

        