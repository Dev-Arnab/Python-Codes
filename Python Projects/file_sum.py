
import re

hand = open("actual_data.txt")
num_list = list()

for line in hand:
    line = line.rstrip()
    numbers = re.findall("[0-9]+", line)
    #if len(numbers) != 1:
    #    continue

    for number in numbers:
        number = int(number)
        num_list.append(number)

print(sum(num_list))

"""
import re

# open the file and read the whole file
with open('actual_data.txt') as f:
    text = f.read()

# find all the numbers in the text using regular expressions. Useful links:-
# https://docs.python.org/3/howto/regex.html
# https://www.w3schools.com/python/python_regex.asp
numbers = re.findall('[0-9]+', text.strip('\n'))

# convert each number string into integer and sum up the list
sum = sum(map(lambda x: int(x), numbers))

print(sum)
"""
