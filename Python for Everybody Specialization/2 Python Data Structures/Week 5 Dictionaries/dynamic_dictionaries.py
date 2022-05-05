#We can do this same thing using get
counts = dict()
names = ["csev", "cwen", "csev", "zquin", "cwen"]

for name in names:
    if name not in counts:
        counts[name] = 1
    else:
        counts[name] = counts[name] + 1
        print(counts)

print(counts)
