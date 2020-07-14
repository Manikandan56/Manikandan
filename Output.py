import csv
import json
import pandas as pd
import sys, getopt, pprint
from pymongo import MongoClient

csvfile = open('myfile.csv','r')
reader = csv.DictReader(csvfile)
mongo_client = MongoClient()
header = ['Transaction_date', 'Product', 'Price', 'Payment_Type', 'Name', 'City', 'State', 'Country', 'Account_created'
    , 'last_login', 'Latutude', 'Longtitude']
for i in reader:
    s = {}
    for j in header:
        s[j] = i[j]
    db.segment.insert(s)
