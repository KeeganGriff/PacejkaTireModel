# D = peak lateral force (abs val) (newtons)
# Ya = value approached asymptotically as x increases (right of D)
# C = 1 +- (1 - (2/pi)(arcsin(Ya/D)))
# then find point on curve closest to (0,0), and its slope. its slope = BCD
# then B = BCD/CD
# Xm is x value of peak D
# E = (BXm - tan(pi/2C))/(BXm - arctan(BXm)), if C > 1

# now we can calculate y = Dsin[C*arctan(Bx - E{Bx - arctan})], where x is slip angle

import pandas as pd
import math as math
import numpy as np

df = pd.read_csv("B2356raw5.csv", sep='\t', skiprows=[0,2], usecols=['SA', 'FY'])
#print(df)

# getting max abs val from lateral force values
D = df['FY'].abs().max()

# don't have line to calc asymptote yet, so will round D down and use that for now
Ya = math.floor(D)
C = 1.3 # pacejka model specifies this as the shape for lateral force?
# C = 1 + (1 - (2/math.pi)*(np.arcsin(Ya/D)))
# if(C < 1):
#     C = 1 - (1 - (2/math.pi)*(np.arcsin(Ya/D)))
