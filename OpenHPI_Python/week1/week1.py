a1 = int(input("Please enter the first angle:"))
a2 = int(input("Please enter the second angle:"))
a3 = int(input("Please enter the third angle:"))

total = a1 + a2 + a3

if total != 180:
        print("The entered values are not valid.")
else:
    if a1 <= 0 or a2 <= 0 or a3 <= 0:
        print("Angles smaller than 0 are not valid.")
    elif a1 < 90 and a2 < 90 and a3 < 90:
        print("The triangle is a acute triangle.")
    elif a1 == 90 or a2 == 90 or a3 == 90:
        print("The triangle is a right triangle.")
    else:
        print("The triangle is a obtuse triangle.")