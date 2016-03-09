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
  offset = 0
  limit = 100
  last = 0
  total = 1

  while last < total:
    data = get_apps(limit, offset)  # download initial list of the apps    
    last = data['last']   # get the last app listed
    total = data['total']   # get the total number of apps

    apps = data['apps']
    ### Print the result
    print_json(apps)

    offset += limit

  # Output the lookup file for the product categories of the apps (Enterprise, Cloud, Lite, Hunk, Enterprise Security)
  product_categories = ['enterprise', 'cloud', 'hunk', 'lite', 'es']
  product_lookup_csv = ''
  for product in product_categories:
    product_offset = 0
    product_apps_last = 0
    product_apps_total = 1

    while product_apps_last < product_apps_total:
      # download initial list of apps within each product category
      apps_product_data = get_apps(limit,product_offset,"product="+product)
      product_apps_last = apps_product_data['last']
      product_apps_total = apps_product_data['total']

      product_apps = apps_product_data['apps']
      product_offset += limit
      
      ### Print the result
      for product_app in list(product_apps):
        # convert it to a csv text
        product_lookup_csv += product + "," + to_csv(product_app) + "\n"

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
