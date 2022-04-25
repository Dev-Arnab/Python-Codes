#Tuples are also a kind of data type
#Tuples can not be modified like lists
#String also can not be modified
"""
t = tuple()
print(dir(t))
"""
"""
d = dict()
d["csev"] = 2
d["cwen"] = 4

for (k,v) in d.items():
    print(k,v)

tups = d.items()
print(tups)
"""

if (0, 1, 2) < (5, 1, 2):
    print(True)
else:
    print(False)

if (0, 1, 2000000) < (0, 3, 4):
    print(True)
else:
    print(False)

if ("Jones", "Sally") < ("Jones", "Sam"):
    print(True)
else:
    print(False)

if ("Jomes", "Sally") > ("Adam", "Sam"):
    print(True)
else:
    print(False)
