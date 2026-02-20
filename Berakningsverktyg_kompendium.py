import matplotlib.pyplot as plt
import sympy as sp
import numpy as np

tal = 9
# %% Default: Användbara kommandon
"""
Beskrivning
"""
modulus = 9%2 # ger resten av 2 hela delningar av 9

# %% Numpy: Användbara kommandon
"""
Från numpy
"""

array = np.array([2,5,7,3])
a2 = np.array([1,1,1,1,1,1])

# tar medelvärdet ur listan
medelvärde = np.average(array) 

# räknar ut standardavvikelsen med hjälp av np.sum()
standardavvikelse = np.sqrt(np.sum(((medelvärde)**2)/len(array))) 

# roten ur ett tal
roten_ur = np.sqrt(tal)

# np.pad "fyller ut" den kortare listan med nollor så att listorna blir lika långa
p1 = np.pad(array, (0,len(a2)-len(array)))









x = np.arange(2019,2026)
#x = [2019, 2022, 2023, 2025]
y = [24300,0,0,26800,0,0,29100]

print(x)
print(y)

plt.scatter(x,y,c ="k")

k = (y[6]-y[0])/(2025-2019)


# plotta en funktion
def func(x):
    print(x,k)
    y_value = k*x + y[0]
    return y_value
    

plt.plot(x,func(x))