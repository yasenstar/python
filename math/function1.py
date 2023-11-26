# Challenge: a + 2ab + b = 22

import numpy as np
import matplotlib.pyplot as mpt

x = []
y = []

for a in range(-100,100):
    for b in range(-100,100):
        if a + 2 * a * b + b == 22:
            x.append(a)
            y.append(b)
            print ("a=", a, " b=", b)

mpt.grid()
mpt.plot(x,y,color="red")
mpt.show()