import sys
from math import exp

h = sys.argv[1]
h = float(h)

p0 = 100.0
h0 = 8400
print(p0 * exp(-h/h0))