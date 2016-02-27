#!/usr/bin/python

### Importing modules
import json
import urllib2

# function that does an http get to download the list of apps that returned in JSON format
def get_apps(limit, offset):
  ### Base URL to download list of apps
  base_url = "https://splunkbase.splunk.com/api/v0/apps/?order=latest&limit="+ str(limit) + "&offset="

  # build the url to download the list of apps
  url = base_url + str(offset)

  ### This takes a python object and dumps it to a string which is a JSON representation of that object
  data = json.load(urllib2.urlopen(url))

  # return the json data
  return data


def main():
  # download initial list of the apps
  data = get_apps(100, 0)

  # get the total number of apps
  total = data['total']

  apps = data['apps']
  ### Print the result
  for app in list(apps):
    jsonText = json.dumps(app, indent=2)
    print jsonText + "\n"

  ### Iterate through all pages to download the json containing a list of apps.
  ### continue downloading the remaining list of apps
  for i, offset in enumerate(range(100, total, 100)):
    # download the list of apps
    data = get_apps(100, offset)

    apps = data['apps']

    ### Print the result
    for app in list(apps):
      jsonText = json.dumps(app, indent=2)
      print jsonText + "\n"


if __name__ == "__main__": main()
