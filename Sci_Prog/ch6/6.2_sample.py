import matplotlib.pyplot as plt
import numpy as np

def f(x):
    return np.exp(-x)*np.sin(2*np.pi*x)

n = 100
x = np.linspace(0, 8, n+1)
y = f(x)

# print(x)
# print(y)

plt.plot(x, y)