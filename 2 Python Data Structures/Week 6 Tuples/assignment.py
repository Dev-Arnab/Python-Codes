file = input("Enter file:")
if len(file) < 1:
    file = "mbox-short.txt"
handle = open(file)

counts = dict()
temp = list()

for line in handle:
    if line.startswith("From "):
        words = line.split()
        time = words[5]
        hours = time[:2]
        counts[hours] = counts.get(hours, 0) + 1

for key, value in counts.items():
    temp.append((key,value))

temp = sorted(temp)

for key,value in temp:
    print(key,value)
