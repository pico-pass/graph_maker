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
        self.init()
        self.show()
    
    def init(self):
        self.fig = plt.figure()
        self.canvas = FigureCanvas(self.fig)
        


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = main_gui()
    app.exec_()