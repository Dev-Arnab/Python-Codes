# To run this, download the BeautifulSoup zip file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

# Take the inputs
url = input('Enter URL: ')
count = int(input("Enter Count: "))
position = int(input("Enter Position: "))


def get_soup(url):
    """Take an URL and return its HTML"""
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
    return soup

# Retrieve all of the anchor tags
for i in range(count):
    soup = get_soup(url)
    anchor_tags = soup.find_all("a")
    url = anchor_tags[position - 1].get("href")
    print(f"Retrieving: {url}")

# Get the name from the last retrieved url
print(url.rsplit('/')[-1].replace('known_by_', '').replace('.html', ''))