###################################################################
# This file  dynamically imports all plugins in the "plugins"     #
# folder based on the config file in each plugin folder.          #
###################################################################

import os
import importlib

lod = os.listdir("./plugins")

name = ''
enabled = ''
activate = ''
startup = ''
deactivate = ''

class setup:
    startList = []
    activeList = []
    deactList = []

    for i in lod:
        with open('./plugins/%s/config' % (i)) as f: #open the plugin config
            lines = f.read().splitlines()
            
            for line in lines:
                exec(line) #set each value in plugin config as variable
            
            if enabled == True:
                
                # import plugin named by config file, but dynamically imports any folder in "plugins" directory
                spec = importlib.util.spec_from_file_location('main', "plugins/%s/main.py" %i) 
                mod = importlib.util.module_from_spec(spec)
                spec.loader.exec_module(mod)
                globals() [name] = mod
                
                # add to startup and/or activate list if enabled in config file
                if startup == True:
                    startList.append(name)
                
                if activate == True:
                    activeList.append(name)
                    
                if deactivate == True:
                    deactList.append(name)

    def dismiss(placeholder):
        for i in setup.deactList:
            return eval(i).deactivate()

    def start(self):
        # start all modules in startlist
        for i in setup.startList:
            eval(i).startup(self)

    def active(dbrow):
        for i in setup.activeList:
            eval(i).activate(dbrow)