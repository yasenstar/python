import matplotlib.pyplot as plt
import numpy as np

formula = input("Wring a mathematical expression of x:")
xmin = float(input("Provide lower bound for x:"))
xmax = float(input("Provide upper bound for x:"))

x = linspace(xmin, xmax, 101)
y = eval(formula)

plt.plot(x, y)
plt.title(f"Plotting your function: {formula}")
plt.show()