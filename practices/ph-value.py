i = 'y'
while i == 'y':
    value = input("Please Enter the PH level: ")
    if len(value) > 0:
        ph = float(value)
        if ph < 7.0:
            print(ph, "is acidic")
        elif ph > 7.0:
            print(ph, "is basic")
        else:
            print(ph, "is neutral")
    else:
        print("no given")
    i = input("continue? (y/n): ")
