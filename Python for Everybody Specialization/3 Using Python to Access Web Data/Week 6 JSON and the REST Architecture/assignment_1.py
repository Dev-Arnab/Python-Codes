import urllib.request, urllib.parse, urllib.error
import json
import ssl

#Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input("Enter Location:")
print("Retrieving", url)
input = urllib.request.urlopen(url, context = ctx).read()

data = json.loads(input)
data = data["comments"]
print("Retrieved", len(data), "characters")

temp = list()
loop_count = 0

for item in data:
    number = item["count"]
    number = int(number)
    temp.append(number)
    loop_count = loop_count + 1

print("Count:", loop_count)

sum =  sum(temp)
print("Sum", sum)
