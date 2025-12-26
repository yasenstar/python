products = [
    ("Dinning Table", 3, 199.90),
    ("Chair", 12, 39.59),
    ("Shelf", 5, 9.90)
]

for product in products:
    print(
        f"{product[0]:15s} Count: {product[1]:3d} Price: {product[2]:6.2f} Total: {product[1]*product[2]:6.2f}"
    )