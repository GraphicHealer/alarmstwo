import os
import importlib

lod = os.listdir("./plugins")

name = ''
enabled = ''
activate = ''
startup = ''

startList = []

activeList = []

for i in lod:
  with open('./plugins/%s/config' % (i)) as f:
    lines = f.read().splitlines()
    for line in lines:
      exec(line)
    if enabled == True:
      spec = importlib.util.spec_from_file_location('main', "plugins/%s/main.py" %i)
      mod = importlib.util.module_from_spec(spec)
      spec.loader.exec_module(mod)
      globals() [name] = mod
      if startup == True:
        startList.append(name)
      if activate == True:
        activeList.append(name)

def start():
  for i in startList:
    eval(i).startup()

def active():
  for i in startList:
    eval(i).activate()