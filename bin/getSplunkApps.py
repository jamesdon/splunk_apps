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
  app_text = ''
  for app in list(apps):
    jsonText = json.dumps(app, indent=2)
    app_text += jsonText + "\n"

  return app_text

# convert the json to a csv for a given set specified fields
def to_csv(apps, product_category='enterprise', headers=['id', 'name']):
  csv_row = ''
  for app in apps:
    csv_str = ''
    # convert it to a csv text
    for field in headers:
      csv_str += app[field] + ","
    
    # remove the last comma
    csv_row += product_category + "," + csv_str.rstrip(',') + "\n"
  return csv_row

def iterate_apps(app_func, app_filter=''):
  offset = 0
  limit = 100
  last = 0
  total = 1

  while last < total:
    data = get_apps(limit, offset, app_filter)  # download initial list of the apps    
    last = data['last']   # get the last app listed
    total = data['total']   # get the total number of apps

    apps = data['apps']
    yield app_func(apps)

    offset += limit

def main():
  app_func = lambda x: print_json(x)
  for app_json in iterate_apps(app_func):
    print app_json

  # Output the lookup file for the product categories of the apps (Enterprise, Cloud, Lite, Hunk, Enterprise Security)
  product_categories = ['enterprise', 'cloud', 'hunk', 'lite', 'es']
  product_lookup_csv = ''
  for product in product_categories:
    product_app_func = lambda product_apps: to_csv(product_apps, product)
    for app_json in iterate_apps(product_app_func, "product="+product):
      product_lookup_csv += app_json

  # append the headers to the csv text
  product_lookup_csv = "Product,Id,Name" + "\n" + product_lookup_csv
  # output the app product csv lookup file to the lookup folder
  lookup_file_name = "splunk_apps_products.csv"
  try:
    lookup_path = os.path.dirname(os.path.realpath(__file__)) + "/.."
  except Exception as e:
    lookup_path = '.'

  lookup_file = lookup_path + "/lookups/" + lookup_file_name
  # debug output file
  # print "message=outputting to " + lookup_file
  f = open(lookup_file, 'w')
  f.write(product_lookup_csv)
  f.close


if __name__ == "__main__": main()
