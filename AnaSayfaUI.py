# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'AnaSayfa.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(821, 742)
        MainWindow.setToolTipDuration(-1)
        MainWindow.setStyleSheet("background-color: rgb(250,235,215)")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(660, 240, 151, 271))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.pushButton_ekle = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_ekle.setStyleSheet("selection-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(0, 0, 0, 255), stop:0.33 rgba(0, 0, 0, 255), stop:0.34 rgba(255, 30, 30, 255), stop:0.66 rgba(255, 0, 0, 255), stop:0.67 rgba(255, 255, 0, 255), stop:1 rgba(255, 255, 0, 255));\n"
"selection-background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(0, 0, 0, 255), stop:0.33 rgba(0, 0, 0, 255), stop:0.34 rgba(255, 30, 30, 255), stop:0.66 rgba(255, 0, 0, 255), stop:0.67 rgba(255, 255, 0, 255), stop:1 rgba(255, 255, 0, 255));\n"
"\n"
"background-color: rgb(240,248,255)")
        self.pushButton_ekle.setObjectName("pushButton_ekle")
        self.verticalLayout_2.addWidget(self.pushButton_ekle)
        self.pushButton_sil = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_sil.setStyleSheet("background-color: rgb(240,248,255)\n"
"")
        self.pushButton_sil.setObjectName("pushButton_sil")
        self.verticalLayout_2.addWidget(self.pushButton_sil)
        self.pushButton_guncelle = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_guncelle.setStyleSheet("background-color: rgb(240,248,255)\n"
"")
        self.pushButton_guncelle.setObjectName("pushButton_guncelle")
        self.verticalLayout_2.addWidget(self.pushButton_guncelle)
        self.pushButton_2 = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_2.setStyleSheet("background-color: rgb(240,248,255)\n"
"")
        self.pushButton_2.setObjectName("pushButton_2")
        self.verticalLayout_2.addWidget(self.pushButton_2)
        self.pushButton_listele = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_listele.setStyleSheet("background-color: rgb(240,248,255)")
        self.pushButton_listele.setObjectName("pushButton_listele")
        self.verticalLayout_2.addWidget(self.pushButton_listele)
        self.layoutWidget1 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget1.setGeometry(QtCore.QRect(30, 170, 388, 361))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.layoutWidget1)
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.groupBox = QtWidgets.QGroupBox(self.layoutWidget1)
        self.groupBox.setStyleSheet("background-color: rgb(240,248,255)\n"
"")
        self.groupBox.setObjectName("groupBox")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.groupBox)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_3.addWidget(self.label_3)
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_5 = QtWidgets.QLabel(self.groupBox)
        self.label_5.setStyleSheet("background-color: rgb(240,248,255)")
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_5.addWidget(self.label_5)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem)
        self.lineEdit = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit.setText("")
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout_5.addWidget(self.lineEdit)
        self.verticalLayout_3.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setStyleSheet("background-color: rgb(240,248,255)")
        self.label.setObjectName("label")
        self.horizontalLayout_6.addWidget(self.label)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem1)
        self.comboBox = QtWidgets.QComboBox(self.groupBox)
        self.comboBox.setToolTipDuration(-1)
        self.comboBox.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.horizontalLayout_6.addWidget(self.comboBox)
        self.verticalLayout_3.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setStyleSheet("background-color: rgb(240,248,255)")
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_7.addWidget(self.label_2)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem2)
        self.comboBox_2 = QtWidgets.QComboBox(self.groupBox)
        self.comboBox_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.horizontalLayout_7.addWidget(self.comboBox_2)
        self.verticalLayout_3.addLayout(self.horizontalLayout_7)
        self.verticalLayout_5.addLayout(self.verticalLayout_3)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_4 = QtWidgets.QLabel(self.groupBox)
        self.label_4.setStyleSheet("background-color: rgb(240,248,255)")
        self.label_4.setObjectName("label_4")
        self.horizontalLayout.addWidget(self.label_4)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem3)
        self.dateEdit = QtWidgets.QDateEdit(self.groupBox)
        self.dateEdit.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.dateEdit.setObjectName("dateEdit")
        self.horizontalLayout.addWidget(self.dateEdit)
        self.verticalLayout_5.addLayout(self.horizontalLayout)
        self.verticalLayout_6.addLayout(self.verticalLayout_5)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_8 = QtWidgets.QLabel(self.groupBox)
        self.label_8.setStyleSheet("background-color: rgb(240,248,255)\n"
"")
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_4.addWidget(self.label_8)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem4)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit_2.setMaxLength(10)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.horizontalLayout_4.addWidget(self.lineEdit_2)
        self.horizontalLayout_2.addLayout(self.horizontalLayout_4)
        self.label_7 = QtWidgets.QLabel(self.groupBox)
        self.label_7.setStyleSheet("background-color: rgb(240,248,255)")
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_2.addWidget(self.label_7)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem5)
        self.comboBox_3 = QtWidgets.QComboBox(self.groupBox)
        self.comboBox_3.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.comboBox_3.setObjectName("comboBox_3")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.horizontalLayout_2.addWidget(self.comboBox_3)
        self.verticalLayout_6.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3.addLayout(self.verticalLayout_6)
        self.verticalLayout_7.addWidget(self.groupBox)
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(-10, 0, 441, 141))
        self.label_9.setText("")
        self.label_9.setPixmap(QtGui.QPixmap("../../Pictures/Screenshots/Ekran görüntüsü 2023-06-02 174153.png"))
        self.label_9.setObjectName("label_9")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(10, 560, 811, 121))
        self.tableWidget.setStyleSheet("background-color: rgb(240,248,255)")
        self.tableWidget.setRowCount(100000)
        self.tableWidget.setColumnCount(15)
        self.tableWidget.setObjectName("tableWidget")
        self.layoutWidget2 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget2.setGeometry(QtCore.QRect(450, 40, 205, 281))
        self.layoutWidget2.setObjectName("layoutWidget2")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.layoutWidget2)
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.label_6 = QtWidgets.QLabel(self.layoutWidget2)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(250, 235, 215))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 213, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 191, 63))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(127, 85, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 113, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(250, 235, 215))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(250, 235, 215))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 212, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(250, 235, 215))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 213, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 191, 63))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(127, 85, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 113, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(250, 235, 215))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(250, 235, 215))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 212, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(127, 85, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(250, 235, 215))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 213, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 191, 63))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(127, 85, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 113, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(127, 85, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(127, 85, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(250, 235, 215))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(250, 235, 215))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 170, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipText, brush)
        self.label_6.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Black")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.verticalLayout_8.addWidget(self.label_6)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.checkBox_izin1 = QtWidgets.QCheckBox(self.layoutWidget2)
        self.checkBox_izin1.setStyleSheet("selection-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, \n"
"\n"
"0, 255), stop:1 rgba(255, 255, 255, 255));\n"
"background-color: rgb(240,248,255)")
        self.checkBox_izin1.setObjectName("checkBox_izin1")
        self.verticalLayout.addWidget(self.checkBox_izin1)
        self.checkBox_izin2 = QtWidgets.QCheckBox(self.layoutWidget2)
        self.checkBox_izin2.setStyleSheet("background-color: rgb(240,248,255)")
        self.checkBox_izin2.setObjectName("checkBox_izin2")
        self.verticalLayout.addWidget(self.checkBox_izin2)
        self.checkBox_izin3 = QtWidgets.QCheckBox(self.layoutWidget2)
        self.checkBox_izin3.setStyleSheet("background-color: rgb(240,248,255)")
        self.checkBox_izin3.setObjectName("checkBox_izin3")
        self.verticalLayout.addWidget(self.checkBox_izin3)
        self.checkBox_izin4 = QtWidgets.QCheckBox(self.layoutWidget2)
        self.checkBox_izin4.setStyleSheet("background-color: rgb(240,248,255)")
        self.checkBox_izin4.setObjectName("checkBox_izin4")
        self.verticalLayout.addWidget(self.checkBox_izin4)
        self.checkBox_izin5 = QtWidgets.QCheckBox(self.layoutWidget2)
        self.checkBox_izin5.setStyleSheet("background-color: rgb(240,248,255)")
        self.checkBox_izin5.setObjectName("checkBox_izin5")
        self.verticalLayout.addWidget(self.checkBox_izin5)
        self.checkBox_izin6 = QtWidgets.QCheckBox(self.layoutWidget2)
        self.checkBox_izin6.setStyleSheet("background-color: rgb(240,248,255)")
        self.checkBox_izin6.setObjectName("checkBox_izin6")
        self.verticalLayout.addWidget(self.checkBox_izin6)
        self.verticalLayout_4.addLayout(self.verticalLayout)
        self.checkBox_izin7 = QtWidgets.QCheckBox(self.layoutWidget2)
        self.checkBox_izin7.setStyleSheet("background-color: rgb(240,248,255)")
        self.checkBox_izin7.setObjectName("checkBox_izin7")
        self.verticalLayout_4.addWidget(self.checkBox_izin7)
        self.checkBox_izin8 = QtWidgets.QCheckBox(self.layoutWidget2)
        self.checkBox_izin8.setStyleSheet("background-color: rgb(240,248,255)")
        self.checkBox_izin8.setObjectName("checkBox_izin8")
        self.verticalLayout_4.addWidget(self.checkBox_izin8)
        self.verticalLayout_8.addLayout(self.verticalLayout_4)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 821, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton_ekle.setText(_translate("MainWindow", "ESER EKLE"))
        self.pushButton_sil.setText(_translate("MainWindow", "ESER SİL"))
        self.pushButton_guncelle.setText(_translate("MainWindow", "ESER GUNCELLE"))
        self.pushButton_2.setToolTip(_translate("MainWindow", "aramanızı sadece kayıt kodu,sadece kayıtlı bölüm veya sadece görevli girişi yaparak sorgulayınız"))
        self.pushButton_2.setText(_translate("MainWindow", "ESER ARA"))
        self.pushButton_listele.setText(_translate("MainWindow", "LİSTELE"))
        self.groupBox.setTitle(_translate("MainWindow", "GENEL BİLGİLER"))
        self.label_5.setText(_translate("MainWindow", "KAYIT KODU"))
        self.label.setText(_translate("MainWindow", "KAYITLI BOLUM"))
        self.comboBox.setItemText(0, _translate("MainWindow", "ARKEOLOJİ"))
        self.comboBox.setItemText(1, _translate("MainWindow", "ETNOGRAFYA"))
        self.comboBox.setItemText(2, _translate("MainWindow", "SANAT"))
        self.comboBox.setItemText(3, _translate("MainWindow", "SANAYİ"))
        self.comboBox.setItemText(4, _translate("MainWindow", "DOĞA"))
        self.comboBox.setItemText(5, _translate("MainWindow", "MUZİK"))
        self.comboBox.setItemText(6, _translate("MainWindow", "TARİH"))
        self.label_2.setText(_translate("MainWindow", "GÖREVLİ"))
        self.comboBox_2.setItemText(0, _translate("MainWindow", "FATİH UÇKAN"))
        self.comboBox_2.setItemText(1, _translate("MainWindow", "MERT MUÇKAN"))
        self.comboBox_2.setItemText(2, _translate("MainWindow", "KEREM KUÇKAN"))
        self.comboBox_2.setItemText(3, _translate("MainWindow", "ENVER TUÇKAN"))
        self.comboBox_2.setItemText(4, _translate("MainWindow", "BUĞRA YUÇKAN"))
        self.comboBox_2.setItemText(5, _translate("MainWindow", "SAİD VUÇKAN"))
        self.label_4.setText(_translate("MainWindow", "GİRİŞ TARİHİ"))
        self.label_8.setText(_translate("MainWindow", "PASS KODU"))
        self.lineEdit_2.setInputMask(_translate("MainWindow", "9999999999"))
        self.label_7.setText(_translate("MainWindow", "SERGİ DÖNEMİ"))
        self.comboBox_3.setItemText(0, _translate("MainWindow", "KALICI"))
        self.comboBox_3.setItemText(1, _translate("MainWindow", "SENELİK "))
        self.comboBox_3.setItemText(2, _translate("MainWindow", "DÖNEMLİK"))
        self.label_6.setText(_translate("MainWindow", "GEREKLİ İZİNLER"))
        self.checkBox_izin1.setText(_translate("MainWindow", "Değişik:RG-24/11/2006-26356"))
        self.checkBox_izin2.setText(_translate("MainWindow", "Değişik:RG-22/11/2007-26356"))
        self.checkBox_izin3.setText(_translate("MainWindow", "Değişik:RG-23/12/2004-26356"))
        self.checkBox_izin4.setText(_translate("MainWindow", " fıkra:RG-24/11/2006-26356"))
        self.checkBox_izin5.setText(_translate("MainWindow", "fıkra:RG-13/01/2006-26356"))
        self.checkBox_izin6.setText(_translate("MainWindow", "RG-24/11/2006-26356"))
        self.checkBox_izin7.setText(_translate("MainWindow", "Mülga:RG-19/1/2012-28178"))
        self.checkBox_izin8.setText(_translate("MainWindow", "Mülga:RF-14/12/2014-28178"))