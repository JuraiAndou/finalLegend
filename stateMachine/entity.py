from mimetypes import init
from stateMachine.agent import Agent
from stateMachine.state import State


class Entity(Agent):
    def __init__(self, state: State, lp: int, dmg: int, m_dmg: int, mp: int) -> None:
        super().__init__(state)
        self.life = lp
        self.damage = dmg
        self.magicDamage = m_dmg
        self.mana = mp
    def execute(self):
        return super().execute()