import random
from itertools import count
import pandas as pd
import matplotlib.pyplot as plt
import serial
from matplotlib.animation import FuncAnimation
import threading
import numpy as np
 
plt.style.use('fivethirtyeight')
arduino_sr = serial.Serial('COM5', '9600')
a = 0
fig = plt.figure
levelcode = turbcode = 0
ax = plt.axes(xlim=(0, 50), ylim=(0, 1024))

max_points = 50
line, = ax.plot(np.arange(max_points),
                np.ones(max_points, dtype=np.float)*np.nan,
                lw=2)

index = count()
wcount = 0
        
def worker():
    global levelcode
    global turbcode
    try:
        if arduino_sr.readable():
            srcode = arduino_sr.readline()
            srcode_i = srcode.decode()
            if '/' in srcode_i:
                turbcode = int(srcode_i.split('/')[0])
                return turbcode
            elif ',' in srcode_i:
                levelcode = int(srcode_i.split(',')[0])
                return levelcode
    except Exception as ex:
        print(ex)
        pass
    return -1
                
def animate(i):
    y = float(worker())
    if(y > -1):
        old_y = line.get_ydata()
        new_y = np.r_[old_y[1:], y]
        line.set_ydata(new_y)
    return line,

thread_serial = threading.Thread(target=worker, args=())
thread_serial.start()

ani = FuncAnimation(plt.gcf(), animate, init_func=lambda: line, interval = 250)

plt.tight_layout()
plt.show()