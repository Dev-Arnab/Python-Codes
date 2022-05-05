import re
"""
x ="My 2 favourite numbers are 19 and 42"
y = re.findall("[0-9]+", x)
# [] means 1 character.
# [0-9] means any number of 1 character
# [0-9]+ means any number of any character
capital_vowels = re.findall("[AEIOU]+", x)
print("Number:",y)
print("Capital Vowels:", capital_vowels)
"""
x = "From: Using the : character"
"""
#Greedy. Will find the largest string
y = re.findall("^F.+:", x)
print(y)
#NOt Greedy. Will return the smallest string
z = re.findall("^F.+?:", x)
print(z)
"""

x = "From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008"
#not whitespace character + @ + not white space character
y = re.findall("\S+@+\S+", x)
print("Email:", y)
#Match using From but extract only the word after space
z = re.findall("^From (\S+@+\S+)", x)
print(z)

domain = re.findall("@([^ ]*)", x)
print(domain)

domain2 = re.findall("^From .*@([^ ]*)", x)
print(domain2)
