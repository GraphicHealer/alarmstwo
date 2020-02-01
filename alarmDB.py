from tinydb import TinyDB, Query
import time
import datetime as dt

db = TinyDB('db.json')

q = Query()

def write(date, time, name, active, sound, vol, *argv):
   
    i = {'date': date, 'time': time, 'name': name, 'active': active, 'sound': sound, 'vol': vol}
    
    for arg in argv:
        a,b = arg.split(':')
        try:
            b = eval(b)
        except:
            b = b
        i[a] = b
    
    db.insert(i)
    
def searchDT(date, time):
    if db.search((q['date'] == date)&(q['time'] == time)) != []:
        s = db.get((q['date'] == date)&(q['time'] == time))
        return s
    else:
        return 'Not Found'

def printDB(clear=0):
    if clear == 1:
        db.purge()
    for i in db:
        print(i)

def cmdline():
    t = input('Please Input Time (13:23:00): ')
    d = input('Please Input Date (mm/dd/yyyy): ')
    name = input('Name your alarm: ')
    active = input('Do you want to enable your alarm? (y/n): ')
    if active == 'y':
        active = True
    elif active == 'n':
        active = False
    mp3 = input('Please type the name of the sound for this alarm (include the extension): ')
    vol = input('Volume (0.0 - 1.0): ')
    print('Setting alarm...')
    write(d, t, name, active, mp3, vol)
    print('Alarm set!')

if __name__ == '__main__':
    cmdline()