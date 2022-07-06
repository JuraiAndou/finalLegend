import random
from stateMachine import State

#Classe de estado que controla o turno do inimigo
class enemyTurn(State):
    def execute(self) -> None:

        if self.agent.mana >= 30:#Há uma execeção de comportamento para caso a mana esteja abaixo do minimo possivel de ser usado.
            #Testa os valores fuzzy e decide o que fazer baseado na maior "vontade"
            if self.agent.atkFuzz.defuzzify() >= self.agent.cureFuzz.defuzzify():
                self.agent.changeState((AtkState()))
            else:
                self.agent.changeState((healState()))
                
            print(f"{type(self.agent).__name__} is on his turn!")
            print(f"{type(self.agent).__name__} is changing state to {type(self.agent._state).__name__}...")
        else:
            self.agent.changeState((AtkState()))
        
        input("enter to skip phase")
        print("________________________________________________________________________________________")
        
#Classe de estado que controla o player
class playerTurn(State):
    def execute(self) -> None:
        print("It's your turn\n\t[1]Attack\n\t[2]heal")
        choice = input("\t:")
        if(int(choice) == 1):
            self.agent.changeState(AtkState())
        elif(int(choice) == 2):
            self.agent.changeState(healState())

class endTurn():
    def execute(self) -> None:
        print(f"{type(self.agent).__name__} is end his turn!")
        self.agent.changeState(waitState())
        input("enter to skip phase")
        print("________________________________________________________________________________________")
        

class waitState(State):#State where one waits for it's turn
    def execute(self) -> None:
        print(f"{type(self.agent).__name__} is waiting for his turn!")
        
        #if(f"{type(self.agent).__name__}" == "Enemy"):
        #     self.agent.changeState(enemyTurn())
        #elif(f"{type(self.agent).__name__}" == "Player"):
            #self.agent.changeState(playerTurn())

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

        if self.agent.life < 0:
            self.agent.changeState(deathState())
        else:
            self.agent.changeState(waitState())
        input("enter to skip phase")
        print("________________________________________________________________________________________")

class AtkState(State):
    def execute(self) -> None:
        print(f"{type(self.agent).__name__} is attacking!")
        self.agent.mana += 10
        
        self.agent.notify()
        self.agent.changeState(endTurn())


class healState(State):
    def execute(self) -> None:
        print(f"{type(self.agent).__name__} is healing!")
        
        if self.agent.mana >= 30:
            if self.agent.life < self.agent.maxLife:
                self.agent.life += 10
                self.agent.mana -= 30
            elif self.agent.life == self.agent.maxLife: 
                print("Não é possivel curar")
            elif self.agent.life >self.agent.maxLife:
                self.agent.life = self.agent.maxLife
        else:
             print("Não é possivel curar")

        input("Press enter")
        self.agent.changeState(endTurn())