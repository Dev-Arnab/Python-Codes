file_name = input("Enter file name: ")
fhand = open(file_name)


for line in fhand:
    line = line.upper().rstrip()
    print(line)
