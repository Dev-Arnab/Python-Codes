fname = input("Enter file name: ")
fh = open(fname)
lst = list()

for line in fh:
    line = line.strip()
    words = line.split()
    for word in words:
        lst.append(word)

my_list = list(dict.fromkeys(lst))
my_list.sort()
print(my_list)
