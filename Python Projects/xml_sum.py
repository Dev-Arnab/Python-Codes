import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
from bs4 import BeautifulSoup
import ssl

#Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input("Enter Location:")
print("Retrieving", url)
input = urllib.request.urlopen(url, context = ctx).read()
print("Retrieved", len(input) ,"characters")
# soup = BeautifulSoup(xml, "XML.parser")

stuff = ET.fromstring(input)
lst = stuff.findall("comments/comment")
#counts = stuff.tree.findall(".//count")

temp = list()
count = 0

for item in lst:
    number = item.find("count").text
    number = int(number)
    temp.append(number)
    count = count + 1

print("Count:", count)

sum = sum(temp)
print("Sum:", sum)
