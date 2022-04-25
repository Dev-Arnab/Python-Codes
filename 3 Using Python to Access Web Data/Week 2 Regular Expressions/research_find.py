#We will write 2 codes which will do the same thing in different method
# ^ means beginning of a line. Or the first character of a line
# . means any character or number
# * means any multiple
# .* means any number of characters maybe one or more than one
# ^X.*: means the beginning of line must be 'X' followed by any number of
# characters and after those there should be a colon
"""
hand = open("mbox-short.txt")
for line in hand:
    line = line.rstrip()
    if line.find("From:") >= 0:
        print(line)
"""
#The second method using regular expression
import re #Importing a library
hand = open("mbox-short.txt")
"""
for line in hand:
    line = line.rstrip()
    if re.search("From:", line):
        print(line)
"""
"""
for line in hand:
    line = line.rstrip()
    if line.startswith("From:"):
        print(line)
"""
"""
for line in hand:
    line = line.rstrip()
    if re.search("^From:", line):
        print(line)
"""
"""
for line in hand:
    line = line.rstrip()
    if re.search("^X.*:", line):
        print(line)
# In the results you will see that there is 'X' in the beginning and after any
# number of characters there is a colon. After colon there might be any chara cter or not
"""

for line in hand:
    line = line.rstrip()
    if re.search("^X-\S+:", line):
        print(line)
#'X-' at the beginning followed by any number of non-white space characters and a colon
