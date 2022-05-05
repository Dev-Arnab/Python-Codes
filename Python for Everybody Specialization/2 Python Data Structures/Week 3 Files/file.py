
fhand = open("mbox-short.txt")
count = 0
"""
for line in fhand:
    line = line.rstrip()
    if line.startswith('From:'):
        count = count + 1
        print(line)
print(count)
"""
#Same code in different methos
"""
for line in fhand:
    line = line.rstrip()
    if not line.startswith("From:"):
        continue
    count = count + 1
    print(line)
print(count)
"""

"""
for line in fhand:
    line = line.rstrip()
    if "@uct.ac.za" in line:
        count = count + 1
        print(line)
print(count)
"""

fname = input("What is the name of the file: ")
try:
    fhand = open(fname)
except:
    print(fname, "can not be opened")
    quit()

for line in fhand:
    if line.startswith("Subject:"):
        count = count + 1
print("There were", count, "subjects in", fname)
