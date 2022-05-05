"""
collection = list()
collection.append("one")
print(collection)

collection.append("2")
print(collection)

collection.append("finish")
print(collection)

collection.sort()
print(collection)
"""

total = list()

while True:
    number = input("Enter a number: ")
    if number == "done":
        break
    number = float(number)
    total.append(number)

print("Average is", sum(total)/len(total))
