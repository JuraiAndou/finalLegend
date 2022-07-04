import random
from stateMachine import State

class enemyTurn(State):#Enemy turn control
    def execute(self) -> None:
        diceRoll = random.choice([AtkState(), healState()])#Fuzzy here
        print(f"{type(self.agent).__name__} is on his turn!")
        print(f"{type(self.agent).__name__} is changing state to {type(diceRoll).__name__}...")
        input("Press enter")
        self.agent.changeState(diceRoll)

class playerTurn(State):#Player turn control
    def execute(self) -> None:
        print("It's your turn\n\t[1]Attack\n\t[2]heal")
        choice = input("\t:")
        if(int(choice) == 1):
            self.agent.changeState(AtkState())
        elif(int(choice) == 2):
            self.agent.changeState(healState())

class waitState(State):#State where one waits for it's turn
    def execute(self) -> None:
        print(f"{type(self.agent).__name__} is waiting for his turn!")
        if(f"{type(self.agent).__name__}" == "Enemy"):
            self.agent.changeState(enemyTurn())
        elif(f"{type(self.agent).__name__}" == "Player"):
            self.agent.changeState(playerTurn())

class deathState(State):
    def execute(self) -> None:
        print(f"{type(self.agent).__name__} is gone!:-(")
        if(f"{type(self.agent).__name__}" == "Enemy"):
            print("You Win!")
        elif(f"{type(self.agent).__name__}" == "Player"):
            print("Game Over...")

class damageState(State):
    _recivedDgm = None
    def __init__(self, dmg: int) -> None:
        super().__init__()
        self._recivedDgm = dmg

    def execute(self) -> None:
        print(f"{type(self.agent).__name__} recived " + str(self._recivedDgm) + " damage!")
        self.agent.life -= self._recivedDgm
        input("Press enter")
        self.agent.changeState(waitState())

class AtkState(State):
    def execute(self) -> None:
        print(f"{type(self.agent).__name__} is attacking!")
        input("Press enter")
        self.agent.notify()
        self.agent.changeState(waitState())

class healState(State):
    def execute(self) -> None:
        print(f"{type(self.agent).__name__} is healing!")

        if self.agent.life < self.agent.maxLife:
            self.agent.life += 3
        elif self.agent.life == self.agent.maxLife: 
            print("Não é possivel curar")
        elif self.agent.life >self.agent.maxLife:
            self.agent.life = self.agent.maxLife

        input("Press enter")
        self.agent.changeState(waitState())