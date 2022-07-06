from stateMachine import Entity, State, Observer

#entidade do inimigo
class Enemy(Entity):
    obs = []#lista de observers
    
    def __init__(self, state: State, lp: int, dmg: int, mp: int) -> None:
        super().__init__(state, lp, dmg, mp)

    #função para o funcinamento do fuzzy
    def addFuzz(self, atkFz, cureFz):
        self.atkFuzz = atkFz
        self.cureFuzz = cureFz

    def execute(self):
        return super().execute()
    
    #metodos do padrão observer
    def addObserver(self, observer: Observer) -> None:
        self.obs.append(observer)
    
    def removeObserver (self, observer: Observer) -> None:
        self.obs.remove(observer)
    
    def notify(self) -> None:
        for observer in self.obs:
            observer.update(self)