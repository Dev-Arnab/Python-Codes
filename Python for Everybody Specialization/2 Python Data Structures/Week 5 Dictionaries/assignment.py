name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)

counts = dict()

for line in handle:
    if line.startswith("From "):
        words = line.split()
        email = words[1]
        counts[email] = counts.get(email, 0) + 1
#print(counts)

biggest_value = None
biggest_key = None

for key,value in counts.items():
    if biggest_value is None or value > biggest_value:
        biggest_key = key
        biggest_value = value

print(biggest_key, biggest_value)
