import matplotlib.pyplot as plt
import sympy as sp
import numpy as np


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