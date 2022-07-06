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

#Esse estado serve somente como um aviso de transição para que o controlado do mundo ("turns") possa definir o quem tem o turno da vez
class endTurn():
    def execute(self) -> None:
        print(f"{type(self.agent).__name__} is end his turn!")
        self.agent.changeState(waitState())
        input("enter to skip phase")
        print("________________________________________________________________________________________")
        
#Esse estado que serve de "idle", onde cada entidade ficará apos deu turno, esperando novamente sua vez
class waitState(State):
    def execute(self) -> None:
        print(f"{type(self.agent).__name__} is waiting for his turn!")

#Esse estado de morte
class deathState(State):
    def execute(self) -> None:
        print(f"{type(self.agent).__name__} is gone!:-(")

        #teste para ver quem morrer e definir se o usuario ganhou ou perdeu
        if(f"{type(self.agent).__name__}" == "Enemy"):
            print("You Win!")
        elif(f"{type(self.agent).__name__}" == "Player"):
            print("Game Over...")

#Estado de dano. Este estado é acesso via um observador que é ativado no estado de ataque.
#Foi feito assim posi precisamos ter acesso ao outro objeto para essa ação, sendo assim, o padrão observer acabou sendo util.
class damageState(State):
    _recivedDgm = None

    def __init__(self, dmg: int) -> None:
        super().__init__()
        self._recivedDgm = dmg

    def execute(self) -> None:
        print(f"{type(self.agent).__name__} recived " + str(self._recivedDgm) + " damage!")
        self.agent.life -= self._recivedDgm

        #testa de a vida é maior que zero para definir se está no deathState ou não.
        if self.agent.life < 0:
            self.agent.changeState(deathState())
        else:
            self.agent.changeState(waitState())
        input("enter to skip phase")
        print("________________________________________________________________________________________")

#Estado de ataque.
class AtkState(State):
    def execute(self) -> None:
        print(f"{type(self.agent).__name__} is attacking!")

        #a cada ataque as entidades restauram 10 de mana caso possivel
        if self.agent.mana < self.agent.maxMana:
            self.agent.mana += 10 
        
        #como falado, para o estado de dano funcionar, durante o estado de ataque de uma das entidades, notificamos os um observador presente no objeto,
        #para que ele tire o dano de seu oponente
        self.agent.notify()
        self.agent.changeState(endTurn())

#Estado de de cura
class healState(State):
    def execute(self) -> None:
        print(f"{type(self.agent).__name__} is healing!")
        
        #Apos testar de o jogador tem mana suficiente para a cura ele efetua a mesma
        if self.agent.mana >= 30:
            #Caso o jogador ja tenha a vida maxima ele não cura
            if self.agent.life < self.agent.maxLife:
                self.agent.life += 10
                self.agent.mana -= 30
            elif self.agent.life == self.agent.maxLife: 
                print("Não é possivel curar")
            elif self.agent.life > self.agent.maxLife: #teste feito para apenas resetar a vida caso ela passe do limite
                self.agent.life = self.agent.maxLife
        else:
             print("Não é possivel curar")

        input("Press enter")
        self.agent.changeState(endTurn())