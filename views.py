# CREATE VIEWS HERE
from django.shortcuts import render
from django.http import HttpResponse
from django.contrib import messages
from django.template import loader
from polls.models import mycollection import csv
def getfile(request):
    if request.method == "POST":
        response=HttpResponse(content_type="text/csv")
        response['Content-Disposition']='attachment'; filename="file.csv"
        database=mycollection.objects.all()
        writer=csv.writer(response)
        rows = 0       D:\DJANGO\PyCharm 2020.1.1\Manikandan
        for mycollection in database:
        writer.writerow(['Transaction_date','Product','Price','Payment_Type','Name','City','State','Country','Account_created'
        ,'last_login','Latutude','Longtitude'])
        rows += 1
        print("A total of",rows,'inserted into MongoDB')
        return HttpResponse("Uploading Completed")
    else:
        print("page not found")





