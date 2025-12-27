try:
    print(5/0)
    break
except:
    print("Sorry, sth wrong...")
except (ValueError, ZeroDivisionError):
    print("Too Bad...")