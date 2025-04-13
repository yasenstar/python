import matplotlib.pyplot as plt
import numpy as np

def f(x, m, s):
    return (1.0/(np.sqrt(2*np.pi)))*(1/s)*np.exp(-0.5*((x-m)/s)**2)

m = 0
s_start = 2
s_stop = 0.2
s_values = np.linspace(s_start, s_stop, 30)

x = np.linspace(m-3*s_start, m+3*s_start, 1000)
max_f = f(m, m, s_stop)

y = f(x, m, s_stop)

lines = plt.plot(x, y)
# print(lines)

plt.axis([x[0], x[-1], -0.1, max_f])
plt.xlabel('x')
plt.ylabel('y')

for s in s_values:
    y = f(x, m, s)
    lines[0].set_ydata(y)
    plt.draw()
    plt.pause(0.5)

# plt.show()