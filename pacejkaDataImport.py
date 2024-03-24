import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Import data from current directory
file = 'B2356raw5.csv'
df = pd.read_csv(file)

# Set first row as column names
df.columns = df.iloc[0]

# Remove first two rows
df = df[2:]

# Set column data types to float
df = df.astype(float)
# df['FY'] = abs(df['FY'])
df['FY'] = -df['FY']

# Group by SA and get max FY
df = df.groupby('SA').median().reset_index()

plt.plot(df['SA'],df['FY'])

# Get smooth curve for plot
# df['FY'] = df['FY'].rolling(window=50).mean()

# plt.plot(df['SA'],df['FY'])

# Create polynomial fit curve
z = np.polyfit(df['SA'], df['FY'], 3)
p = np.poly1d(z)

plt.plot(df['SA'],p(df['SA']),"r--")

D = max(p(df['SA']))

# NEED TO FIND THE VALUE APPROACHED ASYMPTOTICALLY AS X INCREASES
Ya = max(df['SA'])

C = 1 + abs(1-(2/np.pi)*np.arctan(Ya/D))
# Find point on curve closest to (0,0), and its slope. its slope = BCD
X = 0
Y = p(X)
BCD = np.polyder(p)(X)
B = BCD/(C*D)

# Find the value of Xm where p(Xm) = D
Xm = 0
for SA in df['SA']:
    if p(SA) == D:
        Xm = SA
        break

E = (B*Xm - np.tan(np.pi/(2*C)))/(B - np.arctan(B*Xm))
y = D*np.sin(C*np.arctan(B*df['SA'] - E*(B*df['SA'] - np.arctan(B*df['SA']))))

# Print out the coefficients
print("Equation: ", p)
print("D: ", D)
print("C: ", C)
print("Ya: ", Ya)
print("B: ", B)
print("BCD: ", BCD)
print("Xm: ", Xm)
print("E: ", E)

# Plot y
plt.plot(df['SA'],y)

# Show plot
plt.show()
