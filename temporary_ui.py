import random
from itertools import count
import pandas as pd
import matplotlib.pyplot as plt
import serial
from matplotlib.animation import FuncAnimation
import threading
 
plt.style.use('fivethirtyeight')
arduino_sr = serial.Serial('COM5', '9600')
a = 0
x_val = []
y_val = []
 
index = count()
    
def animate(i):
    x_val.append(next(index))
    y_val.append(random.randint(1,10))
    plt.cla()
    plt.plot(x_val, y_val)

ani = FuncAnimation(plt.gcf(), animate, interval = 100)

plt.tight_layout()
plt.show()
