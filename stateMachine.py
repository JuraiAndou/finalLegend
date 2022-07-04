from abc import ABC, abstractmethod

class Agent:
    pass

class Observer(ABC):
    @abstractmethod
    def update(self, agent: Agent) -> None:
        pass

class State(ABC):
    @property
    def agent(self) -> Agent:
        return self._agent

    @agent.setter
    def agent(self, agent: Agent) -> None:
        self._agent = agent
    
    @abstractmethod
    def execute(self) -> None:
        pass


class Agent:
    _state = None
    
    def __init__(self, state : State) -> None:
        self.changeState(state)

    def changeState(self, state: State):
        self._state = state
        self._state.agent = self
    
    def execute(self):
        self._state.execute()

class Entity(Agent):
    def __init__(self, state: State, lp: int, dmg: int, mp: int) -> None:
        super().__init__(state)
        self.maxLife = lp
        self.life = lp
        self.damage = dmg
        self.mana = mp

    def execute(self):
        return super().execute()
    
    @abstractmethod
    def addObserver (self, observer: Observer) -> None:
        pass
    
    @abstractmethod
    def removeObserver (self, observer: Observer) -> None:
        pass
    
    @abstractmethod
    def notify(self) -> None:
        pass

