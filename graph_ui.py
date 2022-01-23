import sys
import serial
import time
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from Ui_GUI import Ui_Form as GUI
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import matplotlib.animation as animation
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
        self.th = thread(parent = self)
        self.th.thread_sg.connect(self.water_display)
        self.init()
        self.show()
    
    def init(self):
        self.fig = plt.figure()
        self.canvas = FigureCanvas(self.fig)
        self.ui.big_brother.addWidget(self.canvas)
        self.fig2 = plt.figure()
        self.canvas2 = FigureCanvas(self.fig2)
        
        self.ui.A_btn.clicked.connect(self.th.make_random)
        
        self.ax = self.fig.add_subplot(211, xlim=(-8, 0), ylim=(0, 1024))
        self.bx = self.fig.add_subplot(212, xlim=(-8, 0), ylim=(0, 1024))
        
    def water_display(self, srnum):
        self.ui.water_display.display(srnum)
        
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