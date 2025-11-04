import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-20,20,100)
y1 = x*25+45
y2 = np.sin(x)

print(x)
print(y1)
print(y2)

# plt.plot(x,y1)
plt.plot(x,y2)

plt.show()