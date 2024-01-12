import numpy as np
import matplotlib.pyplot as plt

# x = np.arange(1,11)
# y = x * 2

x = np.array([2,3,4,5,6])
# y = np.array([4,6,8,10,12])
y=sin(x)
plt.title("test positive ratio")
plt.xlabel("time")
plt.ylabel("distance")
plt.plot(x, y, color="red")
plt.grid()
plt.show()