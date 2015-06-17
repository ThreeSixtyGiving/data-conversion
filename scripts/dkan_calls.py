'''
Rought and ready script to pull all the data from the 360Giving dkan
to a local machine.

Probably needs some work..
'''

import urllib2
import json
import httplib
import os.path
import time


# Used to debug connection info
httplib.HTTPConnection.debuglevel = 1

# Fetch a list of package information from DKAN
base_url = "http://data.threesixtygiving.org/api/3/action/"
url = base_url + "package_list"
request = urllib2.Request(url)
response = urllib2.urlopen(url)
#print(response.headers.dict)
#quit()
data = json.loads(response.read())
print(data)

'''
    Loop through the packages to get the URLs of the data.
    Check if we have a copy already, if not, or if out of date
    then downlad it.

    Note we are only grabbing csv files
'''
for result in data['result']:
    # Use this for testing, jys just grab a single package
    #if result != "blf-grants-data-2004-onwards":
        #continue
    # Fetch a single package, to find the URLs of all the raw data
    url = base_url + "package_show?id=" + result
    print (result)
    response2 = urllib2.urlopen(url)
    data_package = json.loads(response2.read())

    # Find the raw data we want from the resources in the previous data.
    # We only want csvs
    for resource in data_package['result']['resources']:
        if resource['format'] == 'csv':
            print (resource['id'])
            # Now we have the resource, so go and find the URL of the data (at last!
            url = base_url + "resource_show?id=" + resource['id']
            response3 = urllib2.urlopen(url)
            #print(response3.headers.dict)
            #quit()
            data_package2 = json.loads(response3.read())
            data_url = data_package2['result']['url']
            # We have the URL!
            print(data_url)

            # Fetch the data!
            testfile = urllib2.urlopen(data_url)
            #print(testfile.headers.dict) # Get the response headers

            if testfile.headers.get('Last-Modified'):
            # Check to see if file already exists. If so see if it needs
            # grabbing again (check against last modified response)
                if os.path.isfile(result + '.csv'):
                    file_last_modified = time.ctime(os.path.getmtime(result + '.csv'))
                    header_last_modified = testfile.headers.get('Last-Modified')
                    print "last modified: %s" % time.ctime(os.path.getmtime(result + '.csv'))
                    print "created: %s" % time.ctime(os.path.getctime(result + '.csv'))
                    #print('Last Modified response: ' + testfile.headers.get('Last-Modified'))
                    if header_last_modified > file_last_modified:
                        print('Fetching file')
                        data = testfile.read()
                        with open(result + '.csv', 'wb') as code:
                            code.write(data)
                    else:
                        print('File on disk newer than remote. Skip downloading')
                else:  # Fetch file
                    data = testfile.read()
                    with open(result + '.csv', 'wb') as code:
                        code.write(data)
            else:  # Fetch file
                data = testfile.read()
                with open(result + '.csv', 'wb') as code:
                    code.write(data)
