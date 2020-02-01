import logging
import threading
import time
import datetime as dt
import alarmDB as db
import plugins as pl

LogFile = 'alarmLog.txt'

logging.root.handlers = []
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.DEBUG , filename=LogFile)

# set up logging to console
console = logging.StreamHandler()
console.setLevel(logging.INFO)
# set a format which is simpler for console use
formatter = logging.Formatter('%(asctime)s : %(levelname)s : %(message)s')
console.setFormatter(formatter)
logging.getLogger("").addHandler(console)

def activateAlarm(dbrow):
    logging.info('Alarm Active at %s on %s' %(dbrow['date'],dbrow['time']))
    pl.active(dbrow)

def run():
    logging.info("Thread Run: starting")
    while True:
        now = dt.datetime.strptime(dt.datetime.now().strftime("%Y-%m-%d %H:%M:%S"), "%Y-%m-%d %H:%M:%S")
        logging.debug(now)
        
        alarmActive = False
        
        D = dt.datetime.now().strftime("%m/%d/%Y")
        T = dt.datetime.now().strftime("%H:%M:%S")
        dbs = db.searchDT(D, T)
#         print(D, T)
        logging.debug(dbs)
        if dbs != 'Not Found':
            alarmActive = True
        
        if alarmActive == True:
            logging.info("ACTIVE")
            
            a.start()
            time.sleep(1)
        else:
            logging.debug('no')
            time.sleep(0.5)

def stopAlarm():
    return pl.deactive()

def listAlarms():
    col0='IDX'
    col1='Date/Time'
    col2='Name'
    print("%-3s | %-20s | %-20s" %(col0,col1,col2))
    print(('-'*4)+'|'+('-'*22)+'|'+('-'*21))
    for i in db.getAlarms():
        print("%-3s | %-20s | %-20s" %(i[0],i[1],i[2]))

a = threading.Thread(target=activateAlarm, args=[dbs])

y = threading.Thread(target=pl.start)
y.start()

x = threading.Thread(target=run)
x.start()