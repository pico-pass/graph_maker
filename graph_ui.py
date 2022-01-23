import sys
import serial
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from Ui_GUI import Ui_Form as GUI
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import matplotlib.pyplot as plt
import numpy as np

sn = serial.Serial('COM5', '9600') # COM5 부분은 컴퓨터에 따라 다름

class main_gui(QWidget):
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
        self.ui.water_level = QVBoxLayout()
        self.ui.water_level.addWidget(self.canvas)
        
        self.ui.A_btn.clicked.connect(self.th.rt_dplay)
        
    def water_display(self, srnum):
        self.ui.water_display.display(srnum)
        pass
        
class thread(QThread):
    thread_sg = pyqtSignal(int)
    def __init__(self, parent = None):
        super().__init__()
    
    def rt_dplay(self):
        while True:
            srnum = sn
            self.thread_sg.emit(srnum)
            
            
        


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = main_gui()
    app.exec_()