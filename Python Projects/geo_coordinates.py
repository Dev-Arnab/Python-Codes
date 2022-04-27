import urllib.request, urllib.parse, urllib.error
import json
import ssl

#Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

api_key = False
#If you have a Google Places API key, enter it here
#api_key = "AIzaSy___IDByT70"
#https://developers.google.com/maps/documentation/geocoding/intro
if api_key is False:
    api_key = 42
    service_url = "http://py4e-data.dr-chuck.net/json?"
else:
    service_url = "https://maps.googleapis.com/maps/api/geocode/json?"


while True:
    address = input("Enter location:")
    if len(address) < 1:
        break

    parms = dict()
    parms["address"] = address
    if api_key is not False:
        parms["key"] = api_key
    url = service_url + urllib.parse.urlencode(parms)

    print("Retrieving", url)
    uh = urllib.request.urlopen(url)
    data = uh.read().decode()
    print("Retrieved", len(data), "characters")

    try:
        js = json.loads(data)
    except:
        js = None

    if not js or "status" not in js or js["status"] != "OK":
        print("==== Failed To Retrieve ====")
        print(data)
        continue

    print(json.dumps(js, indent = 4))

    lat = js["results"][0]["geometry"]["location"]["lat"]
    lng = js["results"][0]["geometry"]["location"]["lng"]
    print("Lattitude:", lat, "Longitude", lng)
    location = js["results"][0]["formatted_address"]
    print(location)
