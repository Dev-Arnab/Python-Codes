#If you do not specify a delimiter then multiple spaces ware treated as a single spaces
#You can specify what delimeter character to use in the splitting
line_1 = "A lot             of space"
line_1_split_1 = line_1.split()
line_1_split_2 = line_1.split(" ")
print(line_1)
print(len(line_1))
print(line_1_split_1)
print(len(line_1_split_1))
print(line_1_split_2)
print(len(line_1_split_2))

line_2 = "first;second;third"
line_2_split_1 = line_2.split()
line_2_split_2 = line_2.split(";")
print(line_2)
print(len(line_2))
print(line_2_split_1)
print(len(line_2_split_1))
print(line_2_split_2)
print(len(line_2_split_2))
