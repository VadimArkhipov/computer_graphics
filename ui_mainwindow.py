# Form implementation generated from reading ui file 'ui_mainwindow.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        self.openGLWidget = None
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1017, 700)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox = QtWidgets.QGroupBox(parent=self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(670, 20, 221, 91))
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.comboBox = QtWidgets.QComboBox(parent=self.groupBox)
        self.comboBox.setGeometry(QtCore.QRect(10, 40, 191, 31))
        font = QtGui.QFont()
        font.setFamily("Jura")
        font.setPointSize(12)
        self.comboBox.setFont(font)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.label = QtWidgets.QLabel(parent=self.groupBox)
        self.label.setGeometry(QtCore.QRect(10, 10, 181, 16))
        font = QtGui.QFont()
        font.setFamily("Jura")
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.groupBox_2 = QtWidgets.QGroupBox(parent=self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(670, 130, 311, 81))
        font = QtGui.QFont()
        font.setFamily("Jura")
        font.setPointSize(12)
        self.groupBox_2.setFont(font)
        self.groupBox_2.setObjectName("groupBox_2")
        self.checkBox = QtWidgets.QCheckBox(parent=self.groupBox_2)
        self.checkBox.setGeometry(QtCore.QRect(10, 40, 181, 20))
        self.checkBox.setObjectName("checkBox")
        self.groupBox_3 = QtWidgets.QGroupBox(parent=self.centralwidget)
        self.groupBox_3.setGeometry(QtCore.QRect(670, 240, 311, 151))
        font = QtGui.QFont()
        font.setFamily("Jura")
        font.setPointSize(12)
        self.groupBox_3.setFont(font)
        self.groupBox_3.setObjectName("groupBox_3")
        self.comboBox_2 = QtWidgets.QComboBox(parent=self.groupBox_3)
        self.comboBox_2.setGeometry(QtCore.QRect(10, 70, 191, 31))
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.horizontalSlider_3 = QtWidgets.QSlider(parent=self.groupBox_3)
        self.horizontalSlider_3.setGeometry(QtCore.QRect(10, 110, 291, 22))
        self.horizontalSlider_3.setMaximum(100)
        self.horizontalSlider_3.setSingleStep(10)
        self.horizontalSlider_3.setOrientation(QtCore.Qt.Orientation.Horizontal)
        self.horizontalSlider_3.setObjectName("horizontalSlider_3")
        self.checkBox_2 = QtWidgets.QCheckBox(parent=self.groupBox_3)
        self.checkBox_2.setGeometry(QtCore.QRect(10, 30, 181, 20))
        self.checkBox_2.setObjectName("checkBox_2")
        self.groupBox_4 = QtWidgets.QGroupBox(parent=self.centralwidget)
        self.groupBox_4.setGeometry(QtCore.QRect(670, 420, 291, 211))
        font = QtGui.QFont()
        font.setFamily("Jura")
        font.setPointSize(12)
        self.groupBox_4.setFont(font)
        self.groupBox_4.setObjectName("groupBox_4")
        self.label_4 = QtWidgets.QLabel(parent=self.groupBox_4)
        self.label_4.setGeometry(QtCore.QRect(10, 80, 55, 16))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(parent=self.groupBox_4)
        self.label_5.setGeometry(QtCore.QRect(10, 150, 55, 16))
        self.label_5.setObjectName("label_5")
        self.comboBox_3 = QtWidgets.QComboBox(parent=self.groupBox_4)
        self.comboBox_3.setGeometry(QtCore.QRect(10, 170, 261, 31))
        self.comboBox_3.setObjectName("comboBox_3")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_4 = QtWidgets.QComboBox(parent=self.groupBox_4)
        self.comboBox_4.setGeometry(QtCore.QRect(10, 100, 261, 31))
        self.comboBox_4.setObjectName("comboBox_4")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.checkBox_3 = QtWidgets.QCheckBox(parent=self.groupBox_4)
        self.checkBox_3.setGeometry(QtCore.QRect(10, 40, 181, 20))
        self.checkBox_3.setObjectName("checkBox_3")
        self.pushButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(890, 650, 93, 28))
        font = QtGui.QFont()
        font.setFamily("Jura")
        font.setPointSize(12)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "lab2_Arkhipov"))
        self.comboBox.setItemText(0, _translate("MainWindow", "GL_POINTS"))
        self.comboBox.setItemText(1, _translate("MainWindow", "GL_LINES"))
        self.comboBox.setItemText(2, _translate("MainWindow", "GL_LINE_STRIP"))
        self.comboBox.setItemText(3, _translate("MainWindow", "GL_LINE_LOOP"))
        self.comboBox.setItemText(4, _translate("MainWindow", "GL_TRIANGLES"))
        self.comboBox.setItemText(5, _translate("MainWindow", "GL_TRIANGLE_STRIP"))
        self.comboBox.setItemText(6, _translate("MainWindow", "GL_TRIANGLE_FAN"))
        self.comboBox.setItemText(7, _translate("MainWindow", "GL_QUADS"))
        self.comboBox.setItemText(8, _translate("MainWindow", "GL_QUAD_STRIP"))
        self.comboBox.setItemText(9, _translate("MainWindow", "GL_POLYGON"))
        self.comboBox.setItemText(10, _translate("MainWindow", "CIRCLES"))
        self.label.setText(_translate("MainWindow", "Выберите примитив"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Тест отсечения"))
        self.checkBox.setText(_translate("MainWindow", "Активировать"))
        self.groupBox_3.setTitle(_translate("MainWindow", "Тест прозрачности"))
        self.comboBox_2.setItemText(0, _translate("MainWindow", "GL_NEVER"))
        self.comboBox_2.setItemText(1, _translate("MainWindow", "GL_LESS"))
        self.comboBox_2.setItemText(2, _translate("MainWindow", "GL_EQUAL"))
        self.comboBox_2.setItemText(3, _translate("MainWindow", "GL_LEQUAL"))
        self.comboBox_2.setItemText(4, _translate("MainWindow", "GL_GREATER"))
        self.comboBox_2.setItemText(5, _translate("MainWindow", "GL_NOTEQUAL"))
        self.comboBox_2.setItemText(6, _translate("MainWindow", "GL_GEQUAL"))
        self.comboBox_2.setItemText(7, _translate("MainWindow", "GL_ALWAYS"))
        self.checkBox_2.setText(_translate("MainWindow", "Активировать"))
        self.groupBox_4.setTitle(_translate("MainWindow", "Тест смешения цветов"))
        self.label_4.setText(_translate("MainWindow", "sfactor"))
        self.label_5.setText(_translate("MainWindow", "dfactor"))
        self.comboBox_3.setItemText(0, _translate("MainWindow", "GL_ZERO"))
        self.comboBox_3.setItemText(1, _translate("MainWindow", "GL_ONE"))
        self.comboBox_3.setItemText(2, _translate("MainWindow", "GL_SRC_COLOR"))
        self.comboBox_3.setItemText(3, _translate("MainWindow", "GL_ONE_MINUS_SRC_COLOR"))
        self.comboBox_3.setItemText(4, _translate("MainWindow", "GL_SRC_ALPHA"))
        self.comboBox_3.setItemText(5, _translate("MainWindow", "GL_ONE_MINUS_SRC_ALPHA"))
        self.comboBox_3.setItemText(6, _translate("MainWindow", "GL_DST_ALPHA"))
        self.comboBox_3.setItemText(7, _translate("MainWindow", "GL_ONE_MINUS_DST_ALPHA"))
        self.comboBox_4.setItemText(0, _translate("MainWindow", "GL_ZERO"))
        self.comboBox_4.setItemText(1, _translate("MainWindow", "GL_ONE"))
        self.comboBox_4.setItemText(2, _translate("MainWindow", "GL_DST_COLOR"))
        self.comboBox_4.setItemText(3, _translate("MainWindow", "GL_ONE_MINUS_DST_COLOR"))
        self.comboBox_4.setItemText(4, _translate("MainWindow", "GL_SRC_ALPHA"))
        self.comboBox_4.setItemText(5, _translate("MainWindow", "GL_ONE_MINUS_SRC_ALPHA"))
        self.comboBox_4.setItemText(6, _translate("MainWindow", "GL_DST_ALPHA"))
        self.comboBox_4.setItemText(7, _translate("MainWindow", "GL_ONE_MINUS_DST_ALPHA "))
        self.comboBox_4.setItemText(8, _translate("MainWindow", "GL_SRC_ALPHA_SATURATE"))
        self.checkBox_3.setText(_translate("MainWindow", "Активировать"))
        self.pushButton.setText(_translate("MainWindow", "Выход"))
