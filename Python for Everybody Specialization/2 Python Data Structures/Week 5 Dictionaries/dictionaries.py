purse = dict()
purse["money"] = 1500
purse["candy"] = 47
purse["tissues"] = 5
#We can also create an empty dictionary
marks = {"Physics" : 50, "Chemistry" : 49, "Mathematics" : 50}
"""
print(purse)

purse["money"] = purse["money"] - 300
purse["candy"] = purse["candy"] + 50
purse["tissues"] = purse["tissues"] - 1

print(purse)
print(len(purse))
print(purse["candy"])

print(marks)
"""
"""
print(list(marks))
print(marks.keys())
print(marks.values())
print(marks.items())
"""

for aaa, bbb in marks.items():
    print(aaa, bbb)
