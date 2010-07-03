# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'telnetparams.ui'
#
# Created: Sat Jul  3 23:26:46 2010
#      by: PyQt4 UI code generator 4.7.2
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_telnetparams(object):
    def setupUi(self, telnetparams):
        telnetparams.setObjectName("telnetparams")
        telnetparams.resize(587, 214)
        self.buttonBox = QtGui.QDialogButtonBox(telnetparams)
        self.buttonBox.setGeometry(QtCore.QRect(480, 10, 81, 91))
        self.buttonBox.setOrientation(QtCore.Qt.Vertical)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.layoutWidget = QtGui.QWidget(telnetparams)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 20, 451, 161))
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout = QtGui.QGridLayout(self.layoutWidget)
        self.gridLayout.setVerticalSpacing(11)
        self.gridLayout.setObjectName("gridLayout")
        self.label_4 = QtGui.QLabel(self.layoutWidget)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 0, 0, 1, 1)
        self.portnum = QtGui.QLineEdit(self.layoutWidget)
        self.portnum.setObjectName("portnum")
        self.gridLayout.addWidget(self.portnum, 0, 1, 1, 4)
        self.label_5 = QtGui.QLabel(self.layoutWidget)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 1, 0, 1, 1)
        self.loops = QtGui.QSpinBox(self.layoutWidget)
        self.loops.setMinimum(1)
        self.loops.setProperty("value", 3)
        self.loops.setObjectName("loops")
        self.gridLayout.addWidget(self.loops, 1, 1, 1, 1)
        self.label_6 = QtGui.QLabel(self.layoutWidget)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 1, 2, 1, 1)
        self.loopwait = QtGui.QSpinBox(self.layoutWidget)
        self.loopwait.setMinimum(1)
        self.loopwait.setMaximum(300)
        self.loopwait.setObjectName("loopwait")
        self.gridLayout.addWidget(self.loopwait, 1, 3, 1, 2)
        self.label_10 = QtGui.QLabel(self.layoutWidget)
        self.label_10.setObjectName("label_10")
        self.gridLayout.addWidget(self.label_10, 2, 0, 1, 1)
        self.endsleep = QtGui.QSpinBox(self.layoutWidget)
        self.endsleep.setObjectName("endsleep")
        self.gridLayout.addWidget(self.endsleep, 2, 1, 1, 1)
        self.label_11 = QtGui.QLabel(self.layoutWidget)
        self.label_11.setObjectName("label_11")
        self.gridLayout.addWidget(self.label_11, 2, 2, 1, 1)
        self.linger = QtGui.QSpinBox(self.layoutWidget)
        self.linger.setMaximum(99999)
        self.linger.setSingleStep(1000)
        self.linger.setObjectName("linger")
        self.gridLayout.addWidget(self.linger, 2, 3, 1, 2)
        self.label_4.setBuddy(self.portnum)
        self.label_5.setBuddy(self.loops)
        self.label_6.setBuddy(self.loopwait)
        self.label_10.setBuddy(self.endsleep)
        self.label_11.setBuddy(self.linger)

        self.retranslateUi(telnetparams)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("accepted()"), telnetparams.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("rejected()"), telnetparams.reject)
        QtCore.QMetaObject.connectSlotsByName(telnetparams)
        telnetparams.setTabOrder(self.portnum, self.loops)
        telnetparams.setTabOrder(self.loops, self.loopwait)
        telnetparams.setTabOrder(self.loopwait, self.endsleep)
        telnetparams.setTabOrder(self.endsleep, self.linger)
        telnetparams.setTabOrder(self.linger, self.buttonBox)

    def retranslateUi(self, telnetparams):
        telnetparams.setWindowTitle(QtGui.QApplication.translate("telnetparams", "Telnet specific parameters", None, QtGui.QApplication.UnicodeUTF8))
        telnetparams.setToolTip(QtGui.QApplication.translate("telnetparams", "This is the host or IP address of the printer network card", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("telnetparams", "Port &Number", None, QtGui.QApplication.UnicodeUTF8))
        self.portnum.setToolTip(QtGui.QApplication.translate("telnetparams", "This is the port number (or name) to use", None, QtGui.QApplication.UnicodeUTF8))
        self.portnum.setText(QtGui.QApplication.translate("telnetparams", "9100", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("telnetparams", "Conn &attempts", None, QtGui.QApplication.UnicodeUTF8))
        self.loops.setToolTip(QtGui.QApplication.translate("telnetparams", "Number of attempts to be made to connect", None, QtGui.QApplication.UnicodeUTF8))
        self.label_6.setText(QtGui.QApplication.translate("telnetparams", "&waiting", None, QtGui.QApplication.UnicodeUTF8))
        self.loopwait.setToolTip(QtGui.QApplication.translate("telnetparams", "Wait time in between connection attempts", None, QtGui.QApplication.UnicodeUTF8))
        self.loopwait.setSuffix(QtGui.QApplication.translate("telnetparams", " sec", None, QtGui.QApplication.UnicodeUTF8))
        self.label_10.setText(QtGui.QApplication.translate("telnetparams", "Endsleep", None, QtGui.QApplication.UnicodeUTF8))
        self.endsleep.setToolTip(QtGui.QApplication.translate("telnetparams", "In some cases it\'s helpful to sleep at the end of sending a job before closing the connection\n"
"", None, QtGui.QApplication.UnicodeUTF8))
        self.endsleep.setSuffix(QtGui.QApplication.translate("telnetparams", " sec", None, QtGui.QApplication.UnicodeUTF8))
        self.label_11.setText(QtGui.QApplication.translate("telnetparams", "Linger", None, QtGui.QApplication.UnicodeUTF8))
        self.linger.setToolTip(QtGui.QApplication.translate("telnetparams", "Linger time", None, QtGui.QApplication.UnicodeUTF8))
        self.linger.setSuffix(QtGui.QApplication.translate("telnetparams", " ms", None, QtGui.QApplication.UnicodeUTF8))

