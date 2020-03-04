import json
import datetime as dt
import time

def read():
    db = open("db.json", "r+")
    out = db.read()
    db.close()
    return out

def save(data):
    db = open("db.json", "w+")
    json.dump(data, db)
    db.close()
        
def write(typ, time, day, name, active, sound, vol, onetime, *argv):
    
    i = {'type':typ, 'day': day, 'time': time, 'name': name, 'active': active, 'sound': sound, 'vol': vol, 'onetime': onetime}
    
    for arg in argv:
        a,b = arg.split(':')
        try:
            b = eval(b)
        except:
            b = b
        i[a] = b
    
    reads = json.loads(read())
    
    reads['Alarms'].append(i)
    
    save(reads)
    
def searchDT(time):
    todayWeek = dt.datetime.today().strftime('%A')
    todayDate = dt.datetime.now().strftime("%m/%d/%Y")
    s1 = []
    db = json.loads(read())
    for i in db['Alarms']:
        if i['time'] == time:
            s1.append(i)
    for i in s1:
        if i['type'] == 'day' and todayWeek in i['day']:
            if i['onetime']:
                db['Alarms'].remove(i)
                save(db)
            return i
        elif i['type'] == 'date' and i['day'] == todayDate:
            if i['onetime']:
                db['Alarms'].remove(i)
                save(db)
            return i
    return None

def printDB():
    for i in json.loads(read())['Alarms']:
        print(i)
    
def create():
    start =  """
    {
        "Alarms":[]
    }
    """
    save(json.loads(start))
    
def testAdd(amount, startTime, date):
    a, b, c = startTime.split(':')
    for i in range(amount):
        b2 = str(int(b)+i)
        if len(b2) == 1:
            b2 = '0'+b2
        t = a+':'+b2+':'+c
        
        write('date', t, date,'test', True, '.mp3', 1, True)
    
