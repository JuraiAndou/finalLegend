from stateMachine import Observer

class AtkObserver(Observer):
    _atkDgm = None

    def __init__(self, p: Entity, e: Entity) -> None:
        self._atkDgm = dmg
        self.player = p
        self.enemy = e

    def update(self):
        print(f"{type(self.agent).__name__} given " + str(self._atkDgm) + " damage!")

    