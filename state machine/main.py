from abc import ABC, abstractmethod

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
    pass

class Cleanup(State):
    pass

class Idle(State):
    def handle0(self) -> None:
        print('Card inserted. Press 1')
        self.context.transition_to(Security())

class MakeOperation(State):
    pass

class Security(State):
    def handle1(self) -> None:
        print('Checking card ...')
        sleep(3)
        print("Card is correct")
        self.context.transition_to(ChooseOperation())