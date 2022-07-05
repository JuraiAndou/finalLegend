from stateMachine import Entity, State, Observer

class Enemy(Entity):
    obs = []
    
    def __init__(self, state: State, lp: int, dmg: int, mp: int) -> None:
        super().__init__(state, lp, dmg, mp)

    def addFuzz(self, atkFz, cureFz):
        self.atkFuzz = atkFz
        self.cureFuzz = cureFz

    def execute(self):
        return super().execute()
    
    def addObserver(self, observer: Observer) -> None:
        self.obs.append(observer)
    
    def removeObserver (self, observer: Observer) -> None:
        self.obs.remove(observer)
    
    def notify(self) -> None:
        for observer in self.obs:
            observer.update(self)