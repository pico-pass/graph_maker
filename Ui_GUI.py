# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\yumsa\OneDrive\문서\GitHub\graph_maker\GUI.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(733, 571)
        self.gridLayout = QtWidgets.QGridLayout(Form)
        self.gridLayout.setObjectName("gridLayout")
        self.widget_3 = QtWidgets.QWidget(Form)
        self.widget_3.setObjectName("widget_3")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.widget_3)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.entire_widget = QtWidgets.QWidget(self.widget_3)
        self.entire_widget.setObjectName("entire_widget")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.entire_widget)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.water_level = QtWidgets.QVBoxLayout()
        self.water_level.setObjectName("water_level")
        self.horizontalLayout_3.addLayout(self.water_level)
        self.water_turb = QtWidgets.QVBoxLayout()
        self.water_turb.setObjectName("water_turb")
        self.horizontalLayout_3.addLayout(self.water_turb)
        self.verticalLayout_2.addWidget(self.entire_widget)
        self.widget_4 = QtWidgets.QWidget(self.widget_3)
        self.widget_4.setObjectName("widget_4")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.widget_4)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.both = QtWidgets.QWidget(self.widget_4)
        self.both.setObjectName("both")
        self.horizontalLayout_2.addWidget(self.both)
        self.widget = QtWidgets.QWidget(self.widget_4)
        self.widget.setObjectName("widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.water_display = QtWidgets.QLCDNumber(self.widget)
        self.water_display.setObjectName("water_display")
        self.verticalLayout.addWidget(self.water_display)
        self.turb_display = QtWidgets.QLCDNumber(self.widget)
        self.turb_display.setObjectName("turb_display")
        self.verticalLayout.addWidget(self.turb_display)
        self.widget_2 = QtWidgets.QWidget(self.widget)
        self.widget_2.setObjectName("widget_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget_2)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.B_btn = QtWidgets.QPushButton(self.widget_2)
        self.B_btn.setMinimumSize(QtCore.QSize(0, 50))
        self.B_btn.setObjectName("B_btn")
        self.horizontalLayout.addWidget(self.B_btn)
        self.A_btn = QtWidgets.QPushButton(self.widget_2)
        self.A_btn.setMinimumSize(QtCore.QSize(0, 50))
        self.A_btn.setObjectName("A_btn")
        self.horizontalLayout.addWidget(self.A_btn)
        self.verticalLayout.addWidget(self.widget_2)
        self.horizontalLayout_2.addWidget(self.widget)
        self.verticalLayout_2.addWidget(self.widget_4)
        self.gridLayout.addWidget(self.widget_3, 0, 0, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.B_btn.setText(_translate("Form", "B"))
        self.A_btn.setText(_translate("Form", "A"))
