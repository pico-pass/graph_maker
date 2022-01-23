import sys
import serial
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from Ui_GUI import Ui_Form as GUI_FORM
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import numpy as np

sn = serial.Serial('COM5', '9600')

class main_gui(QWidget):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = GUI_FORM
        self.ui.setupUi
        #-------------------------------------#
        
        
        
        
        #-------------------------------------#
        self.show()
        


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = main_gui()
    app.exec_()