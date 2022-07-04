from re import X
import skfuzzy


import numpy as np
import skfuzzy as fuzz

x = np.arange(11)
mfx = fuzz.trimf(x, [0,3,10])