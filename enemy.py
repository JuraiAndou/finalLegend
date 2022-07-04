from stateMachine import Entity, State

class Enemy(Entity):
    def __init__(self, state: State, lp: int, dmg: int, mp: int, obs: List[Observer]) -> None:
        super().__init__(state, lp, dmg, mp, [])

    def execute(self):
        return super().execute()
    
    def addObserver(self, observer: Observer) -> None:
        self.obs.append(observer)
    
    def removeObserver (self, observer: Observer) -> None:
        self.obs.remove(observer)
    
    def notify(self) -> None:
        for observer in self._observers:
            observer.update(self)