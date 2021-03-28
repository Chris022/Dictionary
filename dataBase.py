import sqlite3

from dataTypes import * 



con = sqlite3.connect('data.db')

cur = con.cursor()

cur.execute('''CREATE TABLE IF NOT EXISTS days
               (id integer primary key autoincrement, date text unique, dataChris text, dataKay text);''')

def getEntry(date):
    cur.execute("SELECT date,dataChris,dataKay,id FROM days WHERE date = ?",[date])
    obj = cur.fetchone()
    if(obj == None):
        return {}
    obj = Day(*obj)
    return obj

def addEntry(day:list):
    # Insert a row of data
    cur.execute("INSERT INTO days (date,dataChris,dataKay) VALUES (:date,:dataChris,:dataKay)", day)
    # Save (commit) the changes
    con.commit()

def updateOrCreateEntry(day:list):
    cur.execute("INSERT INTO days (id, date,dataChris,dataKay) VALUES(:id, :date, :dataChris, :dataKay)  ON CONFLICT(date)  DO UPDATE SET dataChris=:dataChris,dataKay=:dataKay;",day)
    
    # Save (commit) the changes
    con.commit()







# We can also close the connection if we are done with it.
# Just be sure any changes have been committed or they will be lost.
#con.close()