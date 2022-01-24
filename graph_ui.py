import sys
import serial
import time
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from Ui_GUI import Ui_Form as GUI
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure as fig
import matplotlib.animation as anim
import matplotlib.pyplot as plt
import numpy as np
import random

# sn = serial.Serial('COM5', '9600') # COM5 부분은 컴퓨터에 따라 다름
sr_num_alpha = 0

class main_gui(QWidget):
    main_stream_signal = pyqtSignal(int)
    def __init__(self):
        super().__init__()
        self.ui = GUI()
        self.ui.setupUi(self)
        
        self.fig = plt.Figure()
        self.canvas = FigureCanvas(self.fig)
        self.timeInterval = 0.2
        
        self.x1 = np.arange(0, 2*np.pi, self.timeInterval)
        self.y1 = np.sin(self.x1)
        
        self.x2 = np.arange(0, 4*np.pi, self.timeInterval)
        self.y2 = np.sin(self.x2)
        
        self.th = thread(parent = self)
        
        self.init()
        self.show()
    
    def init(self):
        self.ui.big_brother.addWidget(self.canvas)
        
        self.ax = self.fig.add_subplot(2,1,1)
        self.line1, = self.ax.plot(self.x1, self.y1)
        self.bx = self.fig.add_subplot(2,1,2)
        self.line2, = self.bx.plot(self.x2, self.y2, color='red')
        
        self.ani1 = anim.FuncAnimation(self.fig, self.animate01, init_func=self.initPlot01, interval=100, blit=False, save_count=50)
        self.canvas.draw()
        self.ani2 = anim.FuncAnimation(self.fig, self.animate02, init_func=self.initPlot02, interval=100, blit=False, save_count=50)
        self.canvas.draw()
        
    def initPlot01(self):
        self.line1.set_ydata([np.nan]*len(self.x1))
        return self.line1,    
    
    def initPlot02(self):
        self.line2.set_ydata([np.nan]*len(self.x2))
        return self.line2,    
    
    def animate01(self, i):        
        self.line1.set_ydata(np.sin(self.x1 + i * self.timeInterval))
        return self.line1,
    
    def animate02(self, i):        
        self.line2.set_ydata(np.sin(self.x2 + i * self.timeInterval))
        return self.line2,
    
class thread(QThread):
    thread_sg = pyqtSignal(int)
    def __init__(self, parent = None):
        super().__init__()
        
    def Qsleep(self, time = 4):
        time = time * 1000
        loop = QEventLoop()
        QTimer.singleShot(time, loop.quit)
        loop.exec_()
        
    def make_random(self):
        while True:
            srnum = random.randint(1, 4)
            self.thread_sg.emit(srnum)
            self.Qsleep(0.5)
    
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = main_gui()
    app.exec_()