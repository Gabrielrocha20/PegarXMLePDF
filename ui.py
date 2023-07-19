# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Uii.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_CompactarNotas(object):
    def setupUi(self, CompactarNotas):
        CompactarNotas.setObjectName("CompactarNotas")
        CompactarNotas.resize(800, 600)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/newPrefix/mw.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        CompactarNotas.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(CompactarNotas)
        self.centralwidget.setMinimumSize(QtCore.QSize(800, 600))
        self.centralwidget.setMaximumSize(QtCore.QSize(800, 600))
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.Windown = QtWidgets.QStackedWidget(self.centralwidget)
        self.Windown.setObjectName("Windown")
        self.Home = QtWidgets.QWidget()
        self.Home.setObjectName("Home")
        self.gridLayout_11 = QtWidgets.QGridLayout(self.Home)
        self.gridLayout_11.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_11.setSpacing(0)
        self.gridLayout_11.setObjectName("gridLayout_11")
        self.frame_4 = QtWidgets.QFrame(self.Home)
        self.frame_4.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.frame_4.setAutoFillBackground(False)
        self.frame_4.setStyleSheet("QFrame{\n"
"    background-color: rgb(255, 255, 255);\n"
"    image: url(:/newPrefix/mw.jpg);\n"
"}\n"
"Spacer{background-color: none;}")
        self.frame_4.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_4.setLineWidth(0)
        self.frame_4.setMidLineWidth(0)
        self.frame_4.setObjectName("frame_4")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.frame_4)
        self.gridLayout_2.setObjectName("gridLayout_2")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem, 0, 2, 1, 1)
        self.frame = QtWidgets.QFrame(self.frame_4)
        self.frame.setMinimumSize(QtCore.QSize(500, 500))
        self.frame.setStyleSheet("QLabel{\n"
"image: none;\n"
"background-color:none\n"
"}\n"
"\n"
"QFrame{\n"
"image: none;\n"
"background-color:none\n"
"}")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName("verticalLayout")
        self.labelColetar = QtWidgets.QLabel(self.frame)
        self.labelColetar.setMaximumSize(QtCore.QSize(16777215, 120))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.labelColetar.setFont(font)
        self.labelColetar.setText("")
        self.labelColetar.setAlignment(QtCore.Qt.AlignCenter)
        self.labelColetar.setObjectName("labelColetar")
        self.verticalLayout.addWidget(self.labelColetar)
        self.labelCompactar = QtWidgets.QLabel(self.frame)
        self.labelCompactar.setMaximumSize(QtCore.QSize(16777215, 120))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.labelCompactar.setFont(font)
        self.labelCompactar.setText("")
        self.labelCompactar.setAlignment(QtCore.Qt.AlignCenter)
        self.labelCompactar.setObjectName("labelCompactar")
        self.verticalLayout.addWidget(self.labelCompactar)
        self.labelFinalizar = QtWidgets.QLabel(self.frame)
        self.labelFinalizar.setMaximumSize(QtCore.QSize(16777215, 120))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.labelFinalizar.setFont(font)
        self.labelFinalizar.setText("")
        self.labelFinalizar.setAlignment(QtCore.Qt.AlignCenter)
        self.labelFinalizar.setObjectName("labelFinalizar")
        self.verticalLayout.addWidget(self.labelFinalizar)
        self.gridLayout_2.addWidget(self.frame, 3, 1, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem1, 0, 0, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem2, 1, 0, 1, 3)
        self.btnGerar = QtWidgets.QPushButton(self.frame_4)
        self.btnGerar.setMinimumSize(QtCore.QSize(100, 100))
        self.btnGerar.setStyleSheet("QPushButton {\n"
"    background-color: rgba(85, 255, 127, 0.5);\n"
"border-radius: 10px\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color: rgb(85, 255, 127);\n"
"}")
        self.btnGerar.setObjectName("btnGerar")
        self.gridLayout_2.addWidget(self.btnGerar, 0, 1, 1, 1)
        self.gridLayout_11.addWidget(self.frame_4, 0, 0, 1, 1)
        self.Windown.addWidget(self.Home)
        self.gridLayout.addWidget(self.Windown, 0, 0, 1, 1)
        CompactarNotas.setCentralWidget(self.centralwidget)

        self.retranslateUi(CompactarNotas)
        self.Windown.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(CompactarNotas)

    def retranslateUi(self, CompactarNotas):
        _translate = QtCore.QCoreApplication.translate
        CompactarNotas.setWindowTitle(_translate("CompactarNotas", "CompactarNotas"))
        self.btnGerar.setText(_translate("CompactarNotas", "Gerar"))
import bg_rc