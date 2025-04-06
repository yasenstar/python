from math import exp
h = input('Please input the altitude (in meters): ')
h = float(h)

p0 = 100.0
h0 = 8400

p = p0 * exp(-h/h0)
print(p)