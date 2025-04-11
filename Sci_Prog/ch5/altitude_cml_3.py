import sys
from math import exp

try:
    h = sys.argv[1]
    h = float(h)
except:
    print("You failed to provide one command line argument!")
    exit()

p0 = 100.0
h0 = 8400
print(p0 * exp(-h/h0))