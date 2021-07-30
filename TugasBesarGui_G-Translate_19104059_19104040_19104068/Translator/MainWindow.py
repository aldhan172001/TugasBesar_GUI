from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 400)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.srcLanguage = QtWidgets.QComboBox(self.centralwidget)
        self.srcLanguage.setObjectName("srcLanguage")
        self.verticalLayout.addWidget(self.srcLanguage)
        self.srcTextEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.srcTextEdit.setObjectName("srcTextEdit")
        self.verticalLayout.addWidget(self.srcTextEdit)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.translateButton = QtWidgets.QPushButton(self.centralwidget)
        self.translateButton.setMinimumSize(QtCore.QSize(95, 64))
        self.translateButton.setMaximumSize(QtCore.QSize(95, 64))
        self.translateButton.setText("")
        self.translateButton.setText("Translate")
        self.translateButton.setObjectName("translateButton")
        self.verticalLayout_3.addWidget(self.translateButton)
        self.horizontalLayout.addLayout(self.verticalLayout_3)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.dstLanguage = QtWidgets.QComboBox(self.centralwidget)
        self.dstLanguage.setObjectName("dstLanguage")
        self.verticalLayout_2.addWidget(self.dstLanguage)
        self.dstTextEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.dstTextEdit.setObjectName("dstTextEdit")
        self.verticalLayout_2.addWidget(self.dstTextEdit)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "G-Translate"))
        self.translateButton.setToolTip(_translate("MainWindow", "G-Translate"))
