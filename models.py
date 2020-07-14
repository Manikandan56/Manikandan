from django.db import models
import pymongo

class my_database(models.Model):

    # CONNECT TO DATABASE
    connection = pymongo.MongoClient('localhost', 27017)

    # CREATE DATABASE
    database = connection['mydatabase']

    # CREATE COLLECTION
    collection = database['mycollection']

    # Insert data
    collection.insert_data = {'Transaction_date', 'Product', ' Price', 'Payment_Type', 'Name', 'City', 'State',
                              'Country', 'Account_created'
        , 'last_login', 'Latitude', 'Longtitude'}

    def get_multiple_data():
        data = collection.find()
        return list(data)
    
A=my_database() 
A.get_multiple_data()


