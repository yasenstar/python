a = float(input("Please enter the value of a:"))
b = float(input("Please enter the value of b:"))
c = float(input("Please enter the value of c:"))

discriminaut = b*b - 4*a*c

if discriminaut == 0:
    print("The quadratic equation has 1 real solution.")
elif discriminaut > 0:
    print("The quadratic equation has 2 real solutions.")
else:
    print("The quadratic equation has 2 complex solutions.")