#!/usr/bin/python

### Importing modules
import json
import urllib2

### Open the URL and the screen name
base_url = "https://splunkbase.splunk.com/api/v0/apps/?order=latest&limit=100&offset="

### Iterate through all pages to download the json containing a list of apps.  
### This will need to be updated after there more than 2,100 Apps.  
### The searches in the dashboard are also tuned to this number.

for i, offset in enumerate(range(0, 2000, 100)):
  url = base_url + str(offset)

  ### This takes a python object and dumps it to a string which is a JSON representation of that object
  data = json.load(urllib2.urlopen(url))

  apps = data['apps']

  ### Print the result
  for app in list(apps):
    jsonText = json.dumps(app, indent=2)
    print jsonText + "\n"



