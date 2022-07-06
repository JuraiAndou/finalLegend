from stateMachine import *
from enetityStates import *

class AtkObserver(Observer):

    def __init__(self, entity: Entity) -> None:
        self.target = entity


    def update(self, agent: Agent):
        print(f"{type(agent).__name__} given " + str(agent.damage) + " damage in " + f"{type(self.target).__name__}" + "!!!")
        self.target.changeState(damageState(agent.damage))
        