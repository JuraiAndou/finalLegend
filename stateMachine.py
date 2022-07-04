from abc import ABC, abstractmethod

class Agent:
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
        #print(f"Agent: {type(self).__name__} Transitioning to {type(state).__name__}")
        self._state = state
        self._state.agent = self
    
    def execute(self):
        self._state.execute()

class Entity(Agent):
    def __init__(self, state: State, lp: int, dmg: int, mp: int) -> None:
        super().__init__(state)
        self.life = lp
        self.damage = dmg
        self.mana = mp
    def execute(self):
        return super().execute()