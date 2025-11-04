import matplotlib.pyplot as plt
import numpy as np

plt.style.use('_mpl-gallery')

x = np.linspace(0,10,30)
y = x**2 + 3*x - 5
plt.plot(x,y)

plt.show()