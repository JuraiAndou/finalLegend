from abc import ABC, abstractmethod
from stateMachine.agent import Agent

class State(ABC):
    @property
    def context(self) -> Agent:
        return self._agent

    @context.setter
    def context(self, context: Agent) -> None:
        pass
    
    @abstractmethod
    def execute(self) -> None:
        pass