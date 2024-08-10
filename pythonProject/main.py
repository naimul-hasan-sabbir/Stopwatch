import tkinter
from datetime import time

counter = 0
running = False

def counter_label(Label):
    def count():
        if running == True:
            global counter
            if counter == 0:
                display = "Starting..."
            else:
                seconds = counter % 60
                minutes = (counter // 60) % 60
                hours = (counter // (60 * 60)) % (60 * 60)

                dt = time(second=seconds, minute=minutes, hour=hours)
                string = dt.isoformat(timespec='auto')
                display = string
            label['text'] = display
            #1000 ms = 1s
            label.after(1000, count)
            counter += 1
    count()

def Start(Label):
    global running
    running = True
    counter_label(label)
    start['state'] = 'disabled'
    stop['state'] = 'normal'
    reset['state'] = 'normal'

def Stop():
    global running
    running = False
    start['state'] = 'normal'
    stop['state'] = 'disabled'
    reset['state'] = 'normal'

def Reset(Label):
    global counter
    counter = 0
    if running == False:
        reset['state'] = 'disabled'
        label['text'] = 'Welcome!'
    else:
        label['text'] = 'Starting...'

root = tkinter.Tk()
root.title("Stopwatch")
root.minsize(width = 250, height = 70)
label = tkinter.Label(root, text = "Welcome!", fg = "black", font = "Verdana 30 bold")

label.pack()
f = tkinter.Frame(root)
start = tkinter.Button(f, text = 'Start', width = 6, command = lambda:Start(label))
stop = tkinter.Button(f, text = 'Stop', width = 6, state = 'disabled',  command = lambda:Stop())
reset = tkinter.Button(f, text = 'Reset', width = 6, state = 'disabled', command = lambda:Reset(label))

f.pack(anchor = 'center', pady = 5)
start.pack(side = "top")
stop.pack(side = "right")
reset.pack(side = "bottom")
root.mainloop()