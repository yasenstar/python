blocks = int(input("Enter the number of blocks: "))

#
# Write your code here.
#	

height = 0

while blocks > 0:
    blocks = blocks - height
    if blocks >= height + 1:
        height = height + 1
    else:
        break

print("The height of the pyramid:", height)