from bottle import Bottle, run, request,static_file,response
from datetime import date, time, datetime
from dateutil import parser, tz

from dataTypes import *
from dataBase import *

import json as jsonF
app = Bottle()

dateDone = date(year=2021, month=7, day=7)


@app.get('/')
def server_static():
    return static_file("index.html", root='./public/day-list/build')

@app.get('/<filepath>')
def server_static(filepath):
    return static_file(filepath, root='./public/day-list/build')

@app.get('/static/js/<filepath>')
def server_static(filepath):
    return static_file(filepath, root='./public/day-list/build/static/js')

@app.get('/days/<datein>')
def getDay(datein):
    l = datein.split("-")
    return jsonF.dumps(getEntry(date(year=int(l[0]), month=int(l[1]), day=int(l[2]))))

@app.get('/today')
def getToday():
    today = date.today()
    return jsonF.dumps(getEntry(today))

@app.get('/daysLeft')
def getDaysLeft():
    today = date.today()
    return jsonF.dumps({"daysleft":f"{(dateDone-today).days}"})

@app.post('/days')
def post():
    data = {"id":request.json.get('id'),"date":str(request.json.get('date')),"dataChris":request.json.get('dataChris'),"dataKay":request.json.get('dataKay')}
    updateOrCreateEntry(data)


run(app, host='localhost', port=8080)

