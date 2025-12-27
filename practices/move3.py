import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

def f(x, m, s):
    return (1.0/(np.sqrt(2*np.pi)*s))*np.exp(-0.5*((x-m)/s)**2)

m = 0
s_start = 2
s_stop = 0.2
s_values = np.linspace(s_start, s_stop, 30)

x = np.linspace(m-3*s_start, m+3*s_start, 1000)

max_f = f(m, m, s_stop)

y = f(x, m, s_stop)

lines = plt.plot(x, y)

def next_frame(s):
    y = f(x,m,s)
    lines[0].set_ydata(y)
    return lines

ani = FuncAnimation(plt.gcf(), next_frame, frames=s_values, interval=100)
plt.show()