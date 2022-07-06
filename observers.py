from stateMachine import *
from enetityStates import *


#oberver de ataque
class AtkObserver(Observer):

    def __init__(self, entity: Entity) -> None:
        #recebe a entidade que ser seu alvo
        self.target = entity

    def update(self, agent: Agent):
        print(f"{type(agent).__name__} given " + str(agent.damage) + " damage in " + f"{type(self.target).__name__}" + "!!!")
        #muda o estado da estidade alvo para o de dano
        self.target.changeState(damageState(agent.damage))
        