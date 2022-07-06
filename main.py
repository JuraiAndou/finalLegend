from __future__ import annotations
from stateMachine import *
from enetityStates import *
from enemy import Enemy
from player import Player
from observers import *
from fuzzy import *

enemy = Enemy(waitState(), lp=100, dmg=10, mp=80)
player = Player(playerTurn(), lp=100, dmg=10, mp=80)

atkEnemyObs = AtkObserver(enemy)
atkPlayerObs = AtkObserver(player)

player.addObserver(atkEnemyObs)
enemy.addObserver(atkPlayerObs)

#fuzzy
atkFuzzy = FuzzAttack(enemy, player)
cureFuzzy = FuzzHeal(enemy)
enemy.addFuzz(atkFuzzy, cureFuzzy)

def painel():
    print("________________________")
    print("|\t[enemy] \t|")
    print("|\tLp:"+str(enemy.life)+" Mp:"+str(enemy.mana)+"\t|")
    print("|\t--------\t|")
    print("|\t[player]\t|")
    print("|\tLp:"+str(player.life)+" Mp:"+str(player.mana)+"\t|")
    print("________________________")

def turn():
    if f"{type(player._state).__name__}" == 'endTurn':
        enemy.changeState(enemyTurn())
        painel()
    
    player.execute()
    
    if f"{type(enemy._state).__name__}" == 'endTurn':
        player.changeState(playerTurn())
        painel()

    enemy.execute()
   

def main():
  
    while (True):
        if(f"{type(player._state).__name__}" == "deathState"):
            print("GameOver!!!!")
            break
        turn()
        if(f"{type(enemy._state).__name__}" == "deathState"):
            print("You Won")
            break

if __name__ == '__main__':
    main()