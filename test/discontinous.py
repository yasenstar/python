import numpy as np
import matplotlib.pyplot as plt

def H(x):
    if x < 0:
        return 0
    else:
        return 1

n = 5
x = np.linspace(-5, 5, n+1)
y = np.zeros(n+1)

for i in range(len(x)):
    y[i] = H(x[i])

plt.plot(x,y)
plt.show()