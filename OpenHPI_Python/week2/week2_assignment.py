init_stock = int(input("Please enter an initial stock level: "))
month_to_plan = int(input("Please enter the number of month to plan: "))

print("The resulting production quantities are:")

for i in range(1,month_to_plan+1):
    stock = init_stock
    psq = int(input("Please enter the planned sales quantity: "))
    if psq <= stock:
        pq = 0
        stock = stock - psq
    else:
        pq = psq - stock
        stock = 0
    init_stock = stock
    print("Production quantity month", i, "-", pq)
