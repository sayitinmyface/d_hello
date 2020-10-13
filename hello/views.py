from django.shortcuts import render
from pymongo import MongoClient

# Create your views here.
def responsewithhtml(req):
    # data = {'first':'yohan','last':'han'}
    data = {}
    data['first'] = req.GET['first']
    data['second'] = req.GET['second']
    return render(req,'hello/responsewithhtml.html',context=data)

# 
def form(req):
    return render(req,'hello/form.html')

# 
def template(req):
    return render(req,'hello/template.html')
# 
def listwithmongo(req):
    db_url = 'mongodb://192.168.219.105:27017'
    data = {}
    with MongoClient(db_url) as clien:
        mydb = clien.mydb
        result = list(mydb.economic.find({}))
        data['page_obj'] = result
    # 
    return render(req,'hello/listwithmongo.html',context=data)