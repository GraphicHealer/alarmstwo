import os
import importlib

lod = os.listdir("./plugins")

lopl = []

for i in lod:
  with open('./plugins/%s/config' % (i)) as f:
    lines = f.read().splitlines()
    for line in lines:
      exec(line)
    if enabled == True:
      lopl.append([name, i, startup, activate])
      globals [name] = importlib.import_module("plugins.%s.main" % i, package='..')

def start():
  for i in lopl:
    print(i)
