import log
from time import sleep
i = 0

while i<999:
    log.log('logging.info', 'TEST-%d'%i)
    i+=1
    sleep(0.01)