# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'window.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(818, 633)
        MainWindow.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.directory = QtWidgets.QLabel(self.centralwidget)
        self.directory.setMaximumSize(QtCore.QSize(100, 100))
        self.directory.setStyleSheet("background-color: rgb(131, 131, 131);\n"
"")
        self.directory.setText("")
        self.directory.setObjectName("directory")
        self.verticalLayout.addWidget(self.directory)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.numpyWindow = QtWidgets.QLabel(self.centralwidget)
        self.numpyWindow.setEnabled(True)
        self.numpyWindow.setMinimumSize(QtCore.QSize(400, 400))
        self.numpyWindow.setMaximumSize(QtCore.QSize(1000, 1000))
        self.numpyWindow.setStyleSheet("background-color: rgb(131, 131, 131);")
        self.numpyWindow.setText("")
        self.numpyWindow.setObjectName("numpyWindow")
        self.horizontalLayout.addWidget(self.numpyWindow)
        self.rmapWindow = QtWidgets.QLabel(self.centralwidget)
        self.rmapWindow.setMinimumSize(QtCore.QSize(400, 400))
        self.rmapWindow.setMaximumSize(QtCore.QSize(1000, 1000))
        self.rmapWindow.setStyleSheet("background-color: rgb(131, 131, 131);")
        self.rmapWindow.setText("")
        self.rmapWindow.setObjectName("rmapWindow")
        self.horizontalLayout.addWidget(self.rmapWindow)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setStyleSheet("background-color: rgb(131, 131, 131);\n"
"")
        self.tableWidget.setRowCount(3)
        self.tableWidget.setColumnCount(5)
        self.tableWidget.setObjectName("tableWidget")
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(180)
        self.tableWidget.verticalHeader().setDefaultSectionSize(50)
        self.verticalLayout.addWidget(self.tableWidget)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.openButton = QtWidgets.QPushButton(self.centralwidget)
        self.openButton.setStyleSheet("background-color: rgb(140, 140, 140);")
        self.openButton.setObjectName("openButton")
        self.horizontalLayout_2.addWidget(self.openButton)
        self.closeButton = QtWidgets.QPushButton(self.centralwidget)
        self.closeButton.setStyleSheet("background-color: rgb(140, 140, 140);")
        self.closeButton.setObjectName("closeButton")
        self.horizontalLayout_2.addWidget(self.closeButton)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.verticalLayout.setStretch(1, 15)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Атлантик.ЗИ"))
        item = self.tableWidget.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", "Точность"))
        item = self.tableWidget.verticalHeaderItem(1)
        item.setText(_translate("MainWindow", "Ошибки I рода"))
        item = self.tableWidget.verticalHeaderItem(2)
        item.setText(_translate("MainWindow", "Ошибки II рода"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Общее"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Неифнормативные участки"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Участки с низкой информативностью"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Среднеинформативные участки"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Участки с высокой информативностью"))
        self.openButton.setText(_translate("MainWindow", "Открыть НЛ ЗИ"))
        self.closeButton.setText(_translate("MainWindow", "Закрыть отображение НЛ ЗИ"))
