from __future__ import annotations
from tracemalloc import stop
from stateMachine import *
from enetityStates import *
from enemy import Enemy
from player import Player
from observers import *
from fuzzy import *

#declaração das entidades
# como o jogador começa primeiro, o estado inicial do jogador é no seu turno, e do inimigo é no turno de espera
enemy = Enemy(waitState(), lp=100, dmg=10, mp=80)
player = Player(playerTurn(), lp=100, dmg=10, mp=80)

#declaração dos observadores, tendo passando como paramentos seu alvo
atkEnemyObs = AtkObserver(enemy)
atkPlayerObs = AtkObserver(player)

#adição dos observadores as suas entidades
player.addObserver(atkEnemyObs)
enemy.addObserver(atkPlayerObs)

#fuzzy
atkFuzzy = FuzzAttack(enemy, player)
cureFuzzy = FuzzHeal(enemy)
enemy.addFuzz(atkFuzzy, cureFuzzy)

#função que exibe uma mini "hud"
def painel():
    print("________________________")
    print("|\t[enemy] \t|")
    print("|\tLp:"+str(enemy.life)+" Mp:"+str(enemy.mana)+"\t|")
    print("|\t--------\t|")
    print("|\t[player]\t|")
    print("|\tLp:"+str(player.life)+" Mp:"+str(player.mana)+"\t|")
    print("________________________")

#função que serve para controlar os turnos
def turn():
    #Esse teste e o proximo consiste em testar se o turno atual de certe entidade esta no seu fim (endTurn), caso esteja, ele aciona a outra entidade para começar seu turno
    if f"{type(player._state).__name__}" == 'endTurn':
        enemy.changeState(enemyTurn())
        painel()
        
    player.execute()#o execute do jogador estar entre os teste pois como ele começa primeiro, o "passo" dele é adiantado, precisando assim atulizar antes do teste de fim de turno.
    
    #testa de o jogagor estar morto e ecessera o game
    if(f"{type(player._state).__name__}" == "deathState"):
            print("GameOver!!!!")
            quit()

    if f"{type(enemy._state).__name__}" == 'endTurn':
        player.changeState(playerTurn())
        painel()
        
    enemy.execute()

    #testa se o inimigo morreu e escerra o game
    if(f"{type(enemy._state).__name__}" == "deathState"):
            print("You Won")
            quit()
   

#gameloop
def main():
    while (True):
        turn()

if __name__ == '__main__':
    main()