import os
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

def activateAlarm(row):
  print(row[2], ':', row[1])

def run():
  logging.info("Thread Run: starting")
  while True:
    now = dt.datetime.strptime(dt.datetime.now().strftime("%Y-%m-%d %H:%M:%S"), "%Y-%m-%d %H:%M:%S")
    logging.debug(now)
    alarmActive = False
    alarmRow = ''
    for row in db.wb().active.values:
      if row[1] == now:
        alarmActive = True
        alarmRow = row
    
    if alarmActive == True:
      logging.info("ACTIVE")
      activateAlarm(alarmRow)
      time.sleep(1)
    else:
      logging.debug('no')
    time.sleep(0.5)

def listAlarms():
  col0='IDX'
  col1='Date/Time'
  col2='Name'
  print("%-3s | %-20s | %-20s" %(col0,col1,col2))
  print(('-'*4)+'|'+('-'*22)+'|'+('-'*21))
  for i in db.getAlarms():
    print("%-3s | %-20s | %-20s" %(i[0],i[1],i[2]))

#x = threading.Thread(target=run)
#x.start()