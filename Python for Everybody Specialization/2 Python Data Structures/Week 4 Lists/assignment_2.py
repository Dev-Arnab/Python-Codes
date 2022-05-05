fname = input("Enter file name: ")
if len(fname) < 1:
    fname = "mbox-short.txt"

fh = open(fname)
count = 0

for line in fh:
    line = line.strip()
    if line.startswith("From "):
        count = count + 1
        words = line.split()
        email = words[1]
        print(email)

print("There were", count, "lines in the file with From as the first word")
