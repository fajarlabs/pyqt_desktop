# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(250, 252)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setStyleSheet("background-color:rgb(255, 255, 255)")
        MainWindow.setDockOptions(QtWidgets.QMainWindow.AllowTabbedDocks|QtWidgets.QMainWindow.AnimatedDocks)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setAutoFillBackground(False)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 231, 241))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_image = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_image.setText("")
        self.label_image.setPixmap(QtGui.QPixmap("login.jpg"))
        self.label_image.setAlignment(QtCore.Qt.AlignCenter)
        self.label_image.setObjectName("label_image")
        self.verticalLayout.addWidget(self.label_image)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label.setMinimumSize(QtCore.QSize(70, 0))
        font = QtGui.QFont()
        font.setFamily("Symbola")
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.horizontalLayout_4.addWidget(self.label)
        self.le_id = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.le_id.setObjectName("le_id")
        self.horizontalLayout_4.addWidget(self.le_id)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_2 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_2.setMinimumSize(QtCore.QSize(70, 0))
        font = QtGui.QFont()
        font.setFamily("Symbola")
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_5.addWidget(self.label_2)
        self.le_password = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.le_password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.le_password.setObjectName("le_password")
        self.horizontalLayout_5.addWidget(self.le_password)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        self.pb_login = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pb_login.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setFamily("Symbola")
        self.pb_login.setFont(font)
        self.pb_login.setObjectName("pb_login")
        self.verticalLayout.addWidget(self.pb_login)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.verticalLayoutWidget.raise_()
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", " "))
        self.label.setText(_translate("MainWindow", "ID"))
        self.label_2.setText(_translate("MainWindow", "Password"))
        self.pb_login.setText(_translate("MainWindow", "Login"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    from LoginModules import Login
    l = Login(ui,MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
