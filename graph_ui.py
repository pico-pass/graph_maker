import sys
import serial
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from Ui_GUI import Ui_Form as GUI
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
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
        self.ui.water_level.addWidget(self.canvas)
        
        self.fig2 = plt.figure()
        self.canvas2 = FigureCanvas(self.fig2)
        self.ui.water_turb.addWidget(self.canvas2)        
        
        self.ui.A_btn.clicked.connect(self.th.make_random)
        
        self.ax = self.canvas.figure.subplots()
        self.ax.plot([0, 1, 2], [1, 1, 2], '-')
        
        self.bx = self.canvas2.figure.subplots()
        self.bx.plot([0, 25, 50, 75, 100], [1, 33, 73, 12, 42], '-')
        
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