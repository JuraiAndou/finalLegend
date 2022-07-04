from __future__ import annotations
from stateMachine import *
from enetityStates import *
from enemy import Enemy

def main():
    enemy = Enemy(AtkState(), lp=100, dmg=5, m_dmg=3, mp=80)
    enemy.execute()
    enemy.execute()

if __name__ == '__main__':
    main()