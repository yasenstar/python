def is_prime(num):
    if num == 2:
        return True
    else:
        for j in range(2,num):
            if num % j == 0:
                return False
        return True

for i in range(1, 20):
	if is_prime(i + 1):
			print(i + 1, end=" ")
print()