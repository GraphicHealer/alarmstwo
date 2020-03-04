import threading
import time
import datetime as dt
import alarmDB as db
import plugins as pl
import log

def activateAlarm(dbrow):
    log.log('logging.info', 'Alarm Active')
    pl.setup.active(dbrow)

def run():
    log.log('logging.info', 'Thread Run: starting')
    while True:
        now = dt.datetime.strptime(dt.datetime.now().strftime("%Y-%m-%d %H:%M:%S"), "%Y-%m-%d %H:%M:%S")
        log.log('logging.debug', now)
        
        alarmActive = False
        
        T = dt.datetime.now().strftime("%H:%M:%S")
        dbs = db.searchDT(T)
        log.log('logging.debug', dbs)
        if dbs != None:
            alarmActive = True
        
        if alarmActive == True:
            log.log('logging.info', 'ACTIVE')
            a = threading.Thread(target=activateAlarm, args=[dbs])
            a.start()
            time.sleep(1)
        else:
            log.log('logging.debug', 'NO')
            time.sleep(0.5)

y = threading.Thread(target=pl.setup().start)
y.start()

x = threading.Thread(target=run)
x.start()