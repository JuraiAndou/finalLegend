from __future__ import annotations
from stateMachine import *
from enetityStates import *
from enemy import Enemy
from player import Player
from observers import *

enemy = Enemy(waitState(), lp=100, dmg=5, mp=80)
player = Player(playerTurn(), lp=100, dmg=5, mp=80)

atkEnemyObs = AtkObserver(enemy)
atkPlayerObs = AtkObserver(Player)

player.addObserver(atkEnemyObs)
enemy.addObserver(atkPlayerObs)

def main():
    while (True):
        print("|\t[enemy] \t|")
        print("|\tLp:"+str(enemy.life)+" Mp:"+str(enemy.mana)+"\t|")
        print("|\t--------\t|")
        print("|\t[player]\t|")
        print("|\tLp:"+str(player.life)+" Mp:"+str(player.mana)+"\t|")
        enemy.execute()
        if(f"{type(enemy._state).__name__}" == "deathState"):
            break
        #print("|\t[enemy] \t|")
        #print("|\tLp:"+str(enemy.life)+" Mp:"+str(enemy.mana)+"\t|")
        #print("|\t--------\t|")
        #print("|\t[player]\t|")
        #print("|\tLp:"+str(player.life)+" Mp:"+str(player.mana)+"\t|")
        player.execute()
        if(f"{type(player._state).__name__}" == "deathState"):
            break

if __name__ == '__main__':
    main()