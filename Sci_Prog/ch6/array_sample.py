import numpy as np
from math import cos
j = np.linspace(0, 1, 11)

print(j, len(j))
for i in range(len(j)):
    y[i] = cos(j[i])
    print(i)
print(y)