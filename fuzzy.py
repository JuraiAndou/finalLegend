import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl
from enemy import *
from player import *

class FuzzAttack:
    def __init__(self, enemy: Enemy, player: Player) -> None:
        self._player = player
        self._enemy = enemy

        self._enemyLP = ctrl.Antecedent(np.arange(0, enemy.maxLife, 1), 'enemyLP')
        self._playerLP = ctrl.Antecedent(np.arange(0, player.maxLife, 1), 'playerLP')
        self._desire = ctrl.Consequent(np.arange(0,101,1), 'desire')

        self._enemyLP.automf(3, 'quant')
        self._playerLP.automf(3, 'quant')

        self._desire['low'] = fuzz.trimf(self._desire.universe, [0,0,35])
        self._desire['average'] = fuzz.trimf(self._desire.universe, [25,35,55])
        self._desire['high'] = fuzz.trimf(self._desire.universe, [55,100,100])
        
        self.rule1 = ctrl.Rule(self._enemyLP['low'] & self._playerLP['high'], self._desire['low'])
        self.rule2 = ctrl.Rule(self._enemyLP['low'] & self._playerLP['average'], self._desire['low'])
        self.rule3 = ctrl.Rule(self._enemyLP['low'] & self._playerLP['low'], self._desire['average'])

        self.rule4 = ctrl.Rule(self._enemyLP['average'] & self._playerLP['high'], self._desire['low'])
        self.rule5 = ctrl.Rule(self._enemyLP['average'] & self._playerLP['average'], self._desire['high'])
        self.rule6 = ctrl.Rule(self._enemyLP['average'] & self._playerLP['low'], self._desire['high'])

        self.rule7 = ctrl.Rule(self._enemyLP['high'] & self._playerLP['high'], self._desire['high'])
        self.rule8 = ctrl.Rule(self._enemyLP['high'] & self._playerLP['average'], self._desire['high'])
        self.rule9 = ctrl.Rule(self._enemyLP['high'] & self._playerLP['low'], self._desire['high'])

        self.defuzz_ctrl = ctrl.ControlSystem([self.rule1,self.rule2,self.rule3,self.rule4,self.rule5,self.rule6,self.rule7,self.rule8,self.rule9])
        self.defuzz = ctrl.ControlSystemSimulation(self.defuzz_ctrl)

    def defuzzify(self):
        self.defuzz.input['enemyLP'] = self._enemy.life
        self.defuzz.input['playerLP'] = self._player.life
        self.defuzz.compute()
        return self.defuzz.output['desire']

class FuzzHeal:
    def __init__(self, enemy: Enemy) -> None:
        self._enemy = enemy
        self._enemyLP = ctrl.Antecedent(np.arange(0, enemy.maxLife, 1), 'enemyLP')
        self._enemyMP = ctrl.Antecedent(np.arange(0, enemy.mana, 1), 'enemyMP')
        self._desire = ctrl.Consequent(np.arange(0,101,1), 'desire')

        self._enemyLP.automf(3, 'quant')
        self._enemyMP.automf(3, 'quant')

        self._desire['low'] = fuzz.trimf(self._desire.universe, [0,0,50])
        self._desire['average'] = fuzz.trimf(self._desire.universe, [0,50,100])
        self._desire['high'] = fuzz.trimf(self._desire.universe, [50,100,100])
        
        self.rule1 = ctrl.Rule(self._enemyLP['low'] & self._enemyMP['high'], self._desire['high'])
        self.rule2 = ctrl.Rule(self._enemyLP['low'] & self._enemyMP['average'], self._desire['high'])
        self.rule3 = ctrl.Rule(self._enemyLP['low'] & self._enemyMP['low'], self._desire['average'])

        self.rule4 = ctrl.Rule(self._enemyLP['average'] & self._enemyMP['high'], self._desire['average'])
        self.rule5 = ctrl.Rule(self._enemyLP['average'] & self._enemyMP['average'], self._desire['average'])
        self.rule6 = ctrl.Rule(self._enemyLP['average'] & self._enemyMP['low'], self._desire['low'])

        self.rule7 = ctrl.Rule(self._enemyLP['high'] & self._enemyMP['high'], self._desire['low'])
        self.rule8 = ctrl.Rule(self._enemyLP['high'] & self._enemyMP['average'], self._desire['low'])
        self.rule9 = ctrl.Rule(self._enemyLP['high'] & self._enemyMP['low'], self._desire['low'])

        self.defuzz_ctrl = ctrl.ControlSystem([self.rule1,self.rule2,self.rule3,self.rule4,self.rule5,self.rule6,self.rule7,self.rule8,self.rule9])
        self.defuzz = ctrl.ControlSystemSimulation(self.defuzz_ctrl)

    def defuzzify(self):
        self.defuzz.input['enemyLP'] = self._enemy.life
        self.defuzz.input['enemyMP'] = self._enemy.mana
        self.defuzz.compute()
        return self.defuzz.output['desire']