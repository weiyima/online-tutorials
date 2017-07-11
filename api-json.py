import urllib.request, urllib.parse, urllib.error
import requests
import json

main_api = 'http://maps.googleapis.com/maps/api/geocode/json?'
address = 'lhr'
url = main_api + urllib.parse.urlencode({'address': address})

# Method 1 - using requests
json_data = requests.get(url).json()
#print(json_data)
#print('Type',type(json_data)) # class 'dict'


# Method 2 - using urllib (my personal preference)
print('==================== using urllib below =============')
uh = urllib.request.urlopen(url) # <class 'http.client.HTTPResponse'>
print('uh type:',type(uh))
data = uh.read().decode() # <class 'str'>
# js = json.loads(data)  # load s == load string of JSON, returns dict

try:
    js = json.loads(data) # <class 'dict'>
except:
    print('Not valid JSON')
    js = None

#print(json.dumps(js, indent=2))  
#print('Type',type(js))

#### extracting data - same since both are python dict ####

json_status = json_data['status']
print('API Status: ',json_status)

if json_status == 'OK' :
    json_address_components = json_data['results'][0]['address_components'] # follows hierarchy of json 
    print(json_address_components) # <class 'dict'>

    for items in json_address_components : 
        # print(items)
        # print('Items type',type(items))
        print(items["long_name"])
