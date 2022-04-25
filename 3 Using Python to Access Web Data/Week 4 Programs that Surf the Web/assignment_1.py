import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

#Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input("Enter: ")
html = urllib.request.urlopen(url, context = ctx).read()
soup = BeautifulSoup(html, "html.parser")

temp = list()
#Retrieve all span tags
spans = soup("span")
for span in spans:
    number = span.contents[0]
    number = int(number)
    temp.append(number)

sum = sum(temp)
print(sum)
