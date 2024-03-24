# D = peak lateral force (abs val) (newtons)
# Ya = value approached asymptotically as x increases (right of D); Lateral Force
# C = 1 +- (1 - (2/pi)(arcsin(Ya/D)))
# then find point on curve closest to (0,0), and its slope. its slope = BCD
# then B = BCD/CD
# Xm is x value of peak D
# E = (BXm - tan(pi/2C))/(BXm - arctan(BXm)), if C > 1

# Y(X) → Cornering force, breaking force, aligning moment
# X → Slip angle, skid ratio
# B → Stiffness factor
# C → Shape factor
# D → Peak value
# E → Curvature factor


# now we can calculate y = Dsin[C*arctan(Bx - E{Bx - arctan})], where x is slip angle

import pandas as pd
import math as math
import numpy as np

df = pd.read_csv("B2356raw5.csv", sep='\t', skiprows=[0,2], usecols=['SA', 'FY'])
#print(df)

# getting max abs val from lateral force values
D = df['FY'].abs().max()
print("D: ", D)
# don't have line to calc asymptote yet, so will round D down and use that for now
Ya = math.floor(D)
C = 1.3 # pacejka model specifies this as the shape for lateral force?

# np.sign returns -1 if C is negative and +1 if C is positive
C = 1 + np.sign(1 - (2/math.pi)*(np.arcsin(Ya/D))) 
print("C: ", C)

# then find point on curve closest to (0,0), and its slope. its slope = BCD
# then B = BCD/CD
closest_point = None
minimum_distance = float('inf') # init to some very large number

for x1, x2 in zip(df['SA'], df['FY']):
    distance = np.sqrt(x1**2 + x2**2)   # use distance formula

    if distance < minimum_distance:
        minimum_distance = distance
        closest_point = (x1, x2)

degree = 3
coeff_p = np.polyfit(df['SA'], df['FY'], degree)


p = np.poly1d(coeff_p)
closest_x1, closest_x2 = closest_point # unpacks tuple
BCD = np.polyder(p)(closest_x1)
B = BCD/(C * D)
print("B: ", B)

Xm = df[df['FY'] == D]['SA'].iloc[0]


# E = (BXm - tan(pi/2C))/(BXm - arctan(BXm)), if C > 1
if C > 1:
    E = ((B * Xm) - np.tan(math.pi/(2 * C)))/((B * Xm) - np.arctan(B * Xm))
else:
    E = None

print("E: ", E)



