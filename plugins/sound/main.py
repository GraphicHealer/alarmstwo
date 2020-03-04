# Sound Plugin

def startup(plug):
    # this is the command to run if you want to dismiss the alarm
    print(plug.deactList)
    plug.dismiss()

def activate(dbrow):
    print('activated')

