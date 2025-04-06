import sys
from math import exp

h = sys.argv[1]
print(h)
h = float(h)

p0 = 100.0
h0 = 8400

p = p0 * exp(-h/h0)
print(p)