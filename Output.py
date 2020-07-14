import csv
import json
import pandas as pd
import sys, getopt, pprint
from pymongo import MongoClient
# Get the csv file
csvfile = open('myfile.csv','r')
# Read the file
reader = csv.DictReader(csvfile)
#MongoDb connection
mongo_client = MongoClient()
#Insert collection in table
header = ['Transaction_date', 'Product', 'Price', 'Payment_Type', 'Name', 'City', 'State', 'Country', 'Account_created'
    , 'last_login', 'Latutude', 'Longtitude']
for i in reader:
    s = {}
    for j in header:
        s[j] = i[j]
    db.segment.insert(s)
