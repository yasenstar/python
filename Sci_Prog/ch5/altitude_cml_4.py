import sys
from math import exp

try:
    h = sys.argv[1]
    h = float(h)
except IndexError:
    print("You failed to provide one command line argument!")
    exit()
except ValueError:
    print(f"We need a pure number, not '{sys.argv[1]}'")
    exit()
except:
    print("something went wrong in reading your inputs")
    exit()

p0 = 100.0
h0 = 8400
print(p0 * exp(-h/h0))