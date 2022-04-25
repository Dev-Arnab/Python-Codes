smallest_so_far = None
print("Before")
list = [9, 41, 12, 3, 74, 15]

for number in list:
    if smallest_so_far is None:
        smallest_so_far = number
    elif number < smallest_so_far:
        smallest_so_far = number
    print(number, smallest_so_far)

print("After", smallest_so_far)
