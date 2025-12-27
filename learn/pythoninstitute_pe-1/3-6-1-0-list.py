my_list = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]
#
# Write your code here.
#
new_list = []

for i in range(len(my_list)):
    if my_list[i] not in new_list:
        new_list.append(my_list[i])
    else:
        continue

print("The list with unique elements only:")
print(new_list)
