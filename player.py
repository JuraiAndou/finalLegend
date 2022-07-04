from stateMachine import Entity, State

class Player(Entity):
    def __init__(self, state: State, lp: int, dmg: int, mp: int) -> None:
        super().__init__(state, lp, dmg, mp)
    
    def execute(self):
        return super().execute()