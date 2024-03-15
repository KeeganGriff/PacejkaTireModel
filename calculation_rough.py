# D = peak lateral force (abs val) (newtons)
# Ya = value approached asymptotically as x increases (right of D)
# C = 1 +- (1 - (2/pi)(arcsin(Ya/D)))
# then find point on curve closest to (0,0), and its slope. its slope = BCD
# then B = BCD/CD
# Xm is x value of peak D
# E = (BXm - tan(pi/2C))/(BXm - arctan(BXm)), if C > 1

# now we can calculate y = Dsin[C*arctan(Bx - E{Bx - arctan})], where x is slip angle

import pandas as pd

df = pd.read_csv("B2356raw5.csv", sep='\t', skiprows=[0,2], usecols=['SA', 'FY'])
print(df)