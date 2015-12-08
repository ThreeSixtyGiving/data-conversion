'''
Rought and ready script to pull all the data from the 360Giving dkan
to a local machine.

Probably needs some work..
'''

import requests
import json
import os.path
import time


# Create a directory to hold the data
data_directory = 'data'
os.makedirs(data_directory, exist_ok=True)

# Fetch a list of package information from DKAN
base_url = "http://data.threesixtygiving.org/api/3/action/"
url = base_url + "current_package_list_with_resources"
request = requests.get(url)
data = request.json()

'''
    Loop through the packages to get the URLs of the data.
    Check if we have a copy already, if not, or if out of date
    then downlad it.

    Note we are only grabbing csv files
'''
for result in data['result']:
    # We need to make another request with the ID https://github.com/ThreeSixtyGiving/data.threesixtygiving.org/issues/11
    response3 = requests.get(base_url + 'package_show?id=' + result['id'])
    data_package = response3.json()

    # Find the raw data we want from the resources in the data.
    # We only want csvs
    for resource in data_package['result']['resources']:
        #if resource['format'] == 'csv':
        print ('Organisation: ' + result['name'])
        print ('Resource: ' + resource['id'])
        # Now we have the resource, so go and find the URL of the data (at last!
        url = base_url + "resource_show?id=" + resource['id']
        print ('DKAN link: ' + url)
        response3 = requests.get(url)
        data_resource = response3.json()
        data_url = data_resource['result']['url']
        # We have the URL!
        print('Link: ' + data_url)

        # Fetch the data!
        testfile = requests.get(data_url)

        os.makedirs(os.path.join(data_directory, result['name']), exist_ok=True)
        # Save file with resource_id as file name
        #output_name = os.path.join(data_directory, result['name'], resource['id'] + '.csv')
        #Save file with last part of data_Url as the file name 
        output_name = os.path.join(data_directory, result['name'], data_url.rsplit('/',1)[-1])

        with open(output_name, 'wb') as fp:
            fp.write(testfile.content)
