import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl

"""
quality = ctrl.Antecedent(np.arange(0,11,1), 'quality')
service = ctrl.Antecedent(np.arange(0,11,1), 'service')
tip = ctrl.Consequent(np.arange(0,101,1), 'tip')

quality.automf(3)
service.automf(3)

tip['low'] = fuzz.trimf(tip.universe, [0, 0, 50])
tip['average'] = fuzz.trimf(tip.universe, [0, 75 ,100])
tip['high'] = fuzz.trimf(tip.universe, [50 ,100, 100])

rule1 = ctrl.Rule(quality['poor'] & service['poor'], tip['low'])
rule2 = ctrl.Rule(quality['average'] & service['average'], tip['average'])
rule3 = ctrl.Rule(quality['good'] & service['good'], tip['high'])

tipping_ctrl = ctrl.ControlSystem([rule1, rule2, rule3])
tipping = ctrl.ControlSystemSimulation(tipping_ctrl)

tipping.input['quality'] = 6.5
tipping.input['service'] = 9.8
tipping.compute()
"""
class FuzzAttack:
    def __init__(self, enemyMaxLP, playerMaxLP) -> None:
        self._enemyLP = ctrl.Antecedent(np.arange(0, enemyMaxLP, 1), 'enemyLP')
        self._playerLP = ctrl.Antecedent(np.arange(0, playerMaxLP, 1), 'playerLP')
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

    def defuzzify(self, enemyLP, playerLP):
        self.defuzz.input['enemyLP'] = enemyLP
        self.defuzz.input['playerLP'] = playerLP
        self.defuzz.compute()
        return self.defuzz.output['desire']

class FuzzHeal:
    def __init__(self, enemyMaxLP, maxMana) -> None:
        self._enemyLP = ctrl.Antecedent(np.arange(0, enemyMaxLP, 1), 'enemyLP')
        self._enemyMP = ctrl.Antecedent(np.arange(0, maxMana, 1), 'enemyMP')
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

    def defuzzify(self, enemyLP, enemyMP):
        self.defuzz.input['enemyLP'] = enemyLP
        self.defuzz.input['enemyMP'] = enemyMP
        self.defuzz.compute()
        return self.defuzz.output['desire']