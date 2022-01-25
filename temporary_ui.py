import random
from itertools import count
import pandas as pd
import matplotlib.pyplot as plt
import serial
from matplotlib.animation import FuncAnimation
import threading
from queue import Queue
 
plt.style.use('fivethirtyeight')
arduino_sr = serial.Serial('COM5', '9600')
a = 0
x_val = []
y_val = []
levelcode = turbcode = 0

q = Queue()
index = count()
lock = threading.Lock()
evt = threading.Event()
wcount = 0
        
def worker(q):
    global wcount
    global levelcode
    global turbcode
    while True:
        wcount += 1
        srcode = arduino_sr.readline()
        srcode_i = srcode.decode()
        if '/' in srcode_i:
            turbcode = int(srcode_i.split('/')[0])
        elif ',' in srcode_i:
            levelcode = int(srcode_i.split(',')[0])
                
        if wcount == 2:
            print("수질센서 : {0} 탁도센서 = {1}".format(levelcode, turbcode))
            q.put(levelcode)
            levelcode = turbcode = 0
            wcount = 0
                
def animate(q):
    global levelcode
    x_val.append(next(index))
    y_val.append(levelcode)
    plt.cla()
    plt.plot(x_val, y_val)

thread_serial = threading.Thread(target=worker, args=(q, ))
thread_serial.start()

ani = FuncAnimation(plt.gcf(), animate, interval = 250)

plt.tight_layout()
plt.show()