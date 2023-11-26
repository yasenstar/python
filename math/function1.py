# Challenge: a + 2ab + b = 22

for a in range(-100,100):
    for b in range(-100,100):
        if a + 2 * a * b + b == 22:
            print ("a=", a, " b=", b)
