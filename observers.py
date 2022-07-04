from stateMachine import *
from enetityStates import *

class AtkObserver(Observer):
    _atkDgm = None

    def __init__(self, entity: Entity) -> None:
        self._atkDgm = 5
        self.target = entity


    def update(self, agent: Agent):
        print(f"{type(agent).__name__} given " + str(self._atkDgm) + " damage! in " + f"{type(self.target).__name__}")
        self.target.changeState(damageState(self._atkDgm))
        
    