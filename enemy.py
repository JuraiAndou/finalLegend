from stateMachine import Entity
from enetityStates import State
class Enemy(Entity):
    def __init__(self, state: State, lp: int, dmg: int, m_dmg: int, mp: int) -> None:
        super().__init__(state, lp, dmg, m_dmg, mp)
    def execute(self):
        return super().execute()