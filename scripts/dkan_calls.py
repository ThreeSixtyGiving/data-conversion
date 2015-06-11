'''
Rough and ready script to pull all the data from the 360Giving dkan
to a local machine.

Probably needs some work..
'''

import urllib, json

base_url = "http://data.threesixtygiving.org/api/3/action/"
url = base_url + "package_list"
response = urllib.urlopen(url);
data = json.loads(response.read())


for result in data['result']: 
    url = base_url + "package_show?id=" + result
    print (result)
    response2 = urllib.urlopen(url);
    data_package = json.loads(response2.read())
    
    for resource in data_package['result']['resources']:
        if resource['format'] == 'csv':
            print (resource['id'])
            url = base_url + "resource_show?id=" + resource['id']
            response3 = urllib.urlopen(url);
            data_package2 = json.loads(response3.read())
            data_url = data_package2['result']['url']
            print(data_url)
            testfile = urllib.URLopener()
            testfile.retrieve(data_url, result + '.csv')
            
