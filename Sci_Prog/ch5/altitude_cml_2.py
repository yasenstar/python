import sys
from math import exp

i = sys.argv

print(type(i))

if len(i) < 2:
    print("You failed to provide one command line argument!")
    exit()

h = sys.argv[1]

print(type(h))

if type(h) == str:
    print("Your input one string, but we need a number")
    exit()

h = float(h)

p0 = 100.0
h0 = 8400
print(p0 * exp(-h/h0))