#We know that, keys in dictionaries remain random and unsorted. We csn use tuples to sort dictionary items
fhand = open("romeo.txt")
count = dict()

for line in fhand:
    words = line.split()
    for word in words:
        count[word] = count.get(word, 0) + 1

# temp = list()
# for key,value in count.items():
#     temp.append((value,key))
# temp = sorted(temp, reverse = True)
#The above code can be done in a single line


temp = sorted([(v,k) for k,v in count.items()], reverse = True)


for value,key in temp[:10]:
    print(key,value)

#We are sorting this based on keys
"""
d = {"a":10, "b":1, "c":22}
print(d.items())

t = sorted(d.items())
print(t)

for k,v in t:
    print(k, v)
"""
"""
#To sort using values, we need to follow this process
c = {"a":10, "b":1, "c":22}
temp = list()

for k,v in c.items():
    temp.append((v,k))

#Sort in ascending order
temp = sorted(temp)
print(temp)

#Sort in descending order
temp = sorted(temp, reverse = True)
print(temp)
"""
