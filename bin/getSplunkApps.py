#!/usr/bin/python

### Importing modules
import json
import urllib2
import os

# function that does an http get to download the list of apps that returned in JSON format
def get_apps(limit, offset, filter=''):
  ### Base URL to download list of apps
  base_url = "https://splunkbase.splunk.com/api/v0/apps/?order=latest&limit="+ str(limit) + "&offset="

  # build the url to download the list of apps
  url = base_url + str(offset) + "&" + filter

  ### This takes a python object and dumps it to a string which is a JSON representation of that object
  data = json.load(urllib2.urlopen(url))

  # return the json data
  return data

# iterate through the list of apps and print the json format
def print_json(apps):
  for app in list(apps):
    jsonText = json.dumps(app, indent=2)
    print jsonText + "\n"

# convert the json to a csv for a given set specified fields
def to_csv(app, headers=['id', 'name']):
  csv_str = ''
  for field in headers:
    csv_str += app[field] + ","
  # remove the last comma
  return csv_str.rstrip(',')

def main():
  # download initial list of the apps
  data = get_apps(100, 0)

  # get the total number of apps
  total = data['total']

  apps = data['apps']
  ### Print the result
  print_json(apps)

  ### Iterate through all pages to download the json containing a list of apps.
  ### continue downloading the remaining list of apps
  for i, offset in enumerate(range(100, total, 100)):
    # download the list of apps
    data = get_apps(100, offset)

    apps = data['apps']
    ### Print the result
    print_json(apps)

  # Output the lookup file for the product categories of the apps (Enterprise, Cloud, Lite, Hunk, Enterprise Security)
  categories = ['enterprise', 'cloud', 'hunk', 'lite', 'es']
  category_lookup_csv = ''
  for category in categories:
    # download initial list of apps within each category
    categorized_apps_data = get_apps(100,0,"product="+category)
    categorized_total = categorized_apps_data['total']

    categorized_apps = categorized_apps_data['apps']
    ### Print the result
    for categorized_app in list(categorized_apps):
      # convert it to a csv text
      category_lookup_csv += category + "," + to_csv(categorized_app) + "\n"

    ### Iterate through all pages to download the json for the given category of apps.
    for i, offset in enumerate(range(100, categorized_total, 100)):
      # download the list of apps
      categorized_apps_data = get_apps(100,offset,"product="+category)

      categorized_apps = categorized_apps_data['apps']
      for categorized_app in list(categorized_apps):
        ### append the result
        category_lookup_csv += category + "," + to_csv(categorized_app) + "\n"

  # append the headers to the csv text
  category_lookup_csv = "Category,Id,Name" + "\n" + category_lookup_csv
  # output the app category csv lookup file to the lookup folder
  lookup_file_name = "splunk_apps_categories.csv"
  try:
    lookup_path = os.path.dirname(os.path.realpath(__file__)) + "/.."
  except Exception as e:
    lookup_path = '.'

  lookup_file = lookup_path + "/lookups/" + lookup_file_name
  # debug output file
  print "message=outputting to " + lookup_file
  f = open(lookup_file, 'w')
  f.write(category_lookup_csv)
  f.close


if __name__ == "__main__": main()
