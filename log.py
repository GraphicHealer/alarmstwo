import logging
import os
import datetime as dt
import zipper
from shutil import copyfile
import glob

LogFile = 'logs/alarmLog.txt'

logging.root.handlers = []
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.DEBUG , filename=LogFile)

# set up logging to console
console = logging.StreamHandler()
console.setLevel(logging.INFO)
# set a format which is simpler for console use
formatter = logging.Formatter('%(asctime)s : %(levelname)s : %(message)s')
console.setFormatter(formatter)
logging.getLogger("").addHandler(console)

def rawcount(filename):
    f = open(filename, 'rb')
    lines = 0
    buf_size = 1024 * 1024
    read_f = f.raw.read

    buf = read_f(buf_size)
    while buf:
        lines += buf.count(b'\n')
        buf = read_f(buf_size)

    return lines

def archive(file, date):
    name = LogFile.split('.txt')
    copyfile(LogFile, name[0]+str(date)+'.txt')
    if len(glob.glob1('./logs',"*.txt")) > 50:
        zipper.archive('./logs', date)
    f = open(file, 'w')
    f.close()

def log(level, value):
    
    eval(level)(value)
    print(rawcount(LogFile))
    if rawcount(LogFile) > 5000:
        archive(LogFile, dt.datetime.now().strftime("%Y-%m-%d_%H-%M-%S"))

archive(LogFile, dt.datetime.now().strftime("%Y-%m-%d_%H-%M-%S"))