# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'test.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(631, 646)
        font = QtGui.QFont()
        font.setPointSize(24)
        MainWindow.setFont(font)
        MainWindow.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.sudoku_field = QtWidgets.QLabel(self.centralwidget)
        self.sudoku_field.setGeometry(QtCore.QRect(0, 0, 631, 571))
        self.sudoku_field.setText("")
        self.sudoku_field.setPixmap(QtGui.QPixmap("sudoku-blankgrid.png"))
        self.sudoku_field.setScaledContents(True)
        self.sudoku_field.setObjectName("sudoku_field")
        self.solve_button = QtWidgets.QPushButton(self.centralwidget)
        self.solve_button.setGeometry(QtCore.QRect(110, 580, 181, 61))
        self.solve_button.setObjectName("solve_button")
        self.clear_button = QtWidgets.QPushButton(self.centralwidget)
        self.clear_button.setGeometry(QtCore.QRect(340, 580, 191, 61))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.clear_button.setFont(font)
        self.clear_button.setObjectName("clear_button")
        self.cell12 = QtWidgets.QLineEdit(self.centralwidget)
        self.cell12.setGeometry(QtCore.QRect(78, 11, 65, 59))
        self.cell12.setCursorPosition(0)
        self.cell12.setPlaceholderText("")
        self.cell12.setObjectName("cell12")
        self.cell11 = QtWidgets.QLineEdit(self.centralwidget)
        self.cell11.setGeometry(QtCore.QRect(11, 11, 65, 59))
        self.cell11.setCursorPosition(0)
        self.cell11.setPlaceholderText("")
        self.cell11.setObjectName("cell11")
        self.cell13 = QtWidgets.QLineEdit(self.centralwidget)
        self.cell13.setGeometry(QtCore.QRect(145, 11, 65, 59))
        self.cell13.setCursorPosition(0)
        self.cell13.setPlaceholderText("")
        self.cell13.setObjectName("cell13")
        self.cell16 = QtWidgets.QLineEdit(self.centralwidget)
        self.cell16.setGeometry(QtCore.QRect(350, 11, 65, 59))
        self.cell16.setCursorPosition(0)
        self.cell16.setPlaceholderText("")
        self.cell16.setObjectName("cell16")
        self.cell15 = QtWidgets.QLineEdit(self.centralwidget)
        self.cell15.setGeometry(QtCore.QRect(283, 11, 65, 59))
        self.cell15.setCursorPosition(0)
        self.cell15.setPlaceholderText("")
        self.cell15.setObjectName("cell15")
        self.cell14 = QtWidgets.QLineEdit(self.centralwidget)
        self.cell14.setGeometry(QtCore.QRect(216, 11, 65, 59))
        self.cell14.setCursorPosition(0)
        self.cell14.setPlaceholderText("")
        self.cell14.setObjectName("cell14")
        self.cell19 = QtWidgets.QLineEdit(self.centralwidget)
        self.cell19.setGeometry(QtCore.QRect(555, 11, 65, 59))
        self.cell19.setCursorPosition(0)
        self.cell19.setPlaceholderText("")
        self.cell19.setObjectName("cell19")
        self.cell18 = QtWidgets.QLineEdit(self.centralwidget)
        self.cell18.setGeometry(QtCore.QRect(488, 11, 65, 59))
        self.cell18.setCursorPosition(0)
        self.cell18.setPlaceholderText("")
        self.cell18.setObjectName("cell18")
        self.cell17 = QtWidgets.QLineEdit(self.centralwidget)
        self.cell17.setGeometry(QtCore.QRect(421, 11, 65, 59))
        self.cell17.setCursorPosition(0)
        self.cell17.setPlaceholderText("")
        self.cell17.setObjectName("cell17")
        self.cell27 = QtWidgets.QLineEdit(self.centralwidget)
        self.cell27.setGeometry(QtCore.QRect(421, 71, 65, 59))
        self.cell27.setCursorPosition(0)
        self.cell27.setPlaceholderText("")
        self.cell27.setObjectName("cell27")
        self.cell25 = QtWidgets.QLineEdit(self.centralwidget)
        self.cell25.setGeometry(QtCore.QRect(283, 71, 65, 59))
        self.cell25.setCursorPosition(0)
        self.cell25.setPlaceholderText("")
        self.cell25.setObjectName("cell25")
        self.cell29 = QtWidgets.QLineEdit(self.centralwidget)
        self.cell29.setGeometry(QtCore.QRect(555, 71, 65, 59))
        self.cell29.setCursorPosition(0)
        self.cell29.setPlaceholderText("")
        self.cell29.setObjectName("cell29")
        self.cell22 = QtWidgets.QLineEdit(self.centralwidget)
        self.cell22.setGeometry(QtCore.QRect(78, 71, 65, 59))
        self.cell22.setCursorPosition(0)
        self.cell22.setPlaceholderText("")
        self.cell22.setObjectName("cell22")
        self.cell23 = QtWidgets.QLineEdit(self.centralwidget)
        self.cell23.setGeometry(QtCore.QRect(145, 71, 65, 59))
        self.cell23.setCursorPosition(0)
        self.cell23.setPlaceholderText("")
        self.cell23.setObjectName("cell23")
        self.cell26 = QtWidgets.QLineEdit(self.centralwidget)
        self.cell26.setGeometry(QtCore.QRect(350, 71, 65, 59))
        self.cell26.setCursorPosition(0)
        self.cell26.setPlaceholderText("")
        self.cell26.setObjectName("cell26")
        self.cell21 = QtWidgets.QLineEdit(self.centralwidget)
        self.cell21.setGeometry(QtCore.QRect(11, 71, 65, 59))
        self.cell21.setCursorPosition(0)
        self.cell21.setPlaceholderText("")
        self.cell21.setObjectName("cell21")
        self.cell28 = QtWidgets.QLineEdit(self.centralwidget)
        self.cell28.setGeometry(QtCore.QRect(488, 71, 65, 59))
        self.cell28.setCursorPosition(0)
        self.cell28.setPlaceholderText("")
        self.cell28.setObjectName("cell28")
        self.cell24 = QtWidgets.QLineEdit(self.centralwidget)
        self.cell24.setGeometry(QtCore.QRect(216, 71, 65, 59))
        self.cell24.setCursorPosition(0)
        self.cell24.setPlaceholderText("")
        self.cell24.setObjectName("cell24")
        self.cell36 = QtWidgets.QLineEdit(self.centralwidget)
        self.cell36.setGeometry(QtCore.QRect(350, 132, 65, 59))
        self.cell36.setCursorPosition(0)
        self.cell36.setPlaceholderText("")
        self.cell36.setObjectName("cell36")
        self.cell34 = QtWidgets.QLineEdit(self.centralwidget)
        self.cell34.setGeometry(QtCore.QRect(216, 132, 65, 59))
        self.cell34.setCursorPosition(0)
        self.cell34.setPlaceholderText("")
        self.cell34.setObjectName("cell34")
        self.cell38 = QtWidgets.QLineEdit(self.centralwidget)
        self.cell38.setGeometry(QtCore.QRect(488, 132, 65, 59))
        self.cell38.setCursorPosition(0)
        self.cell38.setPlaceholderText("")
        self.cell38.setObjectName("cell38")
        self.cell37 = QtWidgets.QLineEdit(self.centralwidget)
        self.cell37.setGeometry(QtCore.QRect(421, 132, 65, 59))
        self.cell37.setCursorPosition(0)
        self.cell37.setPlaceholderText("")
        self.cell37.setObjectName("cell37")
        self.cell35 = QtWidgets.QLineEdit(self.centralwidget)
        self.cell35.setGeometry(QtCore.QRect(283, 132, 65, 59))
        self.cell35.setCursorPosition(0)
        self.cell35.setPlaceholderText("")
        self.cell35.setObjectName("cell35")
        self.cell32 = QtWidgets.QLineEdit(self.centralwidget)
        self.cell32.setGeometry(QtCore.QRect(78, 132, 65, 59))
        self.cell32.setCursorPosition(0)
        self.cell32.setPlaceholderText("")
        self.cell32.setObjectName("cell32")
        self.cell39 = QtWidgets.QLineEdit(self.centralwidget)
        self.cell39.setGeometry(QtCore.QRect(555, 132, 65, 59))
        self.cell39.setCursorPosition(0)
        self.cell39.setPlaceholderText("")
        self.cell39.setObjectName("cell39")
        self.cell33 = QtWidgets.QLineEdit(self.centralwidget)
        self.cell33.setGeometry(QtCore.QRect(145, 132, 65, 59))
        self.cell33.setCursorPosition(0)
        self.cell33.setPlaceholderText("")
        self.cell33.setObjectName("cell33")
        self.cell31 = QtWidgets.QLineEdit(self.centralwidget)
        self.cell31.setGeometry(QtCore.QRect(11, 132, 65, 59))
        self.cell31.setCursorPosition(0)
        self.cell31.setPlaceholderText("")
        self.cell31.setObjectName("cell31")
        self.cell45 = QtWidgets.QLineEdit(self.centralwidget)
        self.cell45.setGeometry(QtCore.QRect(283, 195, 65, 59))
        self.cell45.setCursorPosition(0)
        self.cell45.setPlaceholderText("")
        self.cell45.setObjectName("cell45")
        self.cell41 = QtWidgets.QLineEdit(self.centralwidget)
        self.cell41.setGeometry(QtCore.QRect(11, 195, 65, 59))
        self.cell41.setCursorPosition(0)
        self.cell41.setPlaceholderText("")
        self.cell41.setObjectName("cell41")
        self.cell68 = QtWidgets.QLineEdit(self.centralwidget)
        self.cell68.setGeometry(QtCore.QRect(488, 317, 65, 59))
        self.cell68.setCursorPosition(0)
        self.cell68.setPlaceholderText("")
        self.cell68.setObjectName("cell68")
        self.cell53 = QtWidgets.QLineEdit(self.centralwidget)
        self.cell53.setGeometry(QtCore.QRect(145, 256, 65, 59))
        self.cell53.setCursorPosition(0)
        self.cell53.setPlaceholderText("")
        self.cell53.setObjectName("cell53")
        self.cell54 = QtWidgets.QLineEdit(self.centralwidget)
        self.cell54.setGeometry(QtCore.QRect(216, 256, 65, 59))
        self.cell54.setCursorPosition(0)
        self.cell54.setPlaceholderText("")
        self.cell54.setObjectName("cell54")
        self.cell58 = QtWidgets.QLineEdit(self.centralwidget)
        self.cell58.setGeometry(QtCore.QRect(488, 256, 65, 59))
        self.cell58.setCursorPosition(0)
        self.cell58.setPlaceholderText("")
        self.cell58.setObjectName("cell58")
        self.cell48 = QtWidgets.QLineEdit(self.centralwidget)
        self.cell48.setGeometry(QtCore.QRect(488, 195, 65, 59))
        self.cell48.setCursorPosition(0)
        self.cell48.setPlaceholderText("")
        self.cell48.setObjectName("cell48")
        self.cell56 = QtWidgets.QLineEdit(self.centralwidget)
        self.cell56.setGeometry(QtCore.QRect(350, 256, 65, 59))
        self.cell56.setCursorPosition(0)
        self.cell56.setPlaceholderText("")
        self.cell56.setObjectName("cell56")
        self.cell47 = QtWidgets.QLineEdit(self.centralwidget)
        self.cell47.setGeometry(QtCore.QRect(421, 195, 65, 59))
        self.cell47.setCursorPosition(0)
        self.cell47.setPlaceholderText("")
        self.cell47.setObjectName("cell47")
        self.cell66 = QtWidgets.QLineEdit(self.centralwidget)
        self.cell66.setGeometry(QtCore.QRect(350, 317, 65, 59))
        self.cell66.setCursorPosition(0)
        self.cell66.setPlaceholderText("")
        self.cell66.setObjectName("cell66")
        self.cell64 = QtWidgets.QLineEdit(self.centralwidget)
        self.cell64.setGeometry(QtCore.QRect(216, 317, 65, 59))
        self.cell64.setCursorPosition(0)
        self.cell64.setPlaceholderText("")
        self.cell64.setObjectName("cell64")
        self.cell62 = QtWidgets.QLineEdit(self.centralwidget)
        self.cell62.setGeometry(QtCore.QRect(78, 317, 65, 59))
        self.cell62.setCursorPosition(0)
        self.cell62.setPlaceholderText("")
        self.cell62.setObjectName("cell62")
        self.cell59 = QtWidgets.QLineEdit(self.centralwidget)
        self.cell59.setGeometry(QtCore.QRect(555, 256, 65, 59))
        self.cell59.setCursorPosition(0)
        self.cell59.setPlaceholderText("")
        self.cell59.setObjectName("cell59")
        self.cell55 = QtWidgets.QLineEdit(self.centralwidget)
        self.cell55.setGeometry(QtCore.QRect(283, 256, 65, 59))
        self.cell55.setCursorPosition(0)
        self.cell55.setPlaceholderText("")
        self.cell55.setObjectName("cell55")
        self.cell46 = QtWidgets.QLineEdit(self.centralwidget)
        self.cell46.setGeometry(QtCore.QRect(350, 195, 65, 59))
        self.cell46.setCursorPosition(0)
        self.cell46.setPlaceholderText("")
        self.cell46.setObjectName("cell46")
        self.cell44 = QtWidgets.QLineEdit(self.centralwidget)
        self.cell44.setGeometry(QtCore.QRect(216, 195, 65, 59))
        self.cell44.setCursorPosition(0)
        self.cell44.setPlaceholderText("")
        self.cell44.setObjectName("cell44")
        self.cell51 = QtWidgets.QLineEdit(self.centralwidget)
        self.cell51.setGeometry(QtCore.QRect(11, 256, 65, 59))
        self.cell51.setCursorPosition(0)
        self.cell51.setPlaceholderText("")
        self.cell51.setObjectName("cell51")
        self.cell52 = QtWidgets.QLineEdit(self.centralwidget)
        self.cell52.setGeometry(QtCore.QRect(78, 256, 65, 59))
        self.cell52.setCursorPosition(0)
        self.cell52.setPlaceholderText("")
        self.cell52.setObjectName("cell52")
        self.cell65 = QtWidgets.QLineEdit(self.centralwidget)
        self.cell65.setGeometry(QtCore.QRect(283, 317, 65, 59))
        self.cell65.setCursorPosition(0)
        self.cell65.setPlaceholderText("")
        self.cell65.setObjectName("cell65")
        self.cell69 = QtWidgets.QLineEdit(self.centralwidget)
        self.cell69.setGeometry(QtCore.QRect(555, 317, 65, 59))
        self.cell69.setCursorPosition(0)
        self.cell69.setPlaceholderText("")
        self.cell69.setObjectName("cell69")
        self.cell42 = QtWidgets.QLineEdit(self.centralwidget)
        self.cell42.setGeometry(QtCore.QRect(78, 195, 65, 59))
        self.cell42.setCursorPosition(0)
        self.cell42.setPlaceholderText("")
        self.cell42.setObjectName("cell42")
        self.cell49 = QtWidgets.QLineEdit(self.centralwidget)
        self.cell49.setGeometry(QtCore.QRect(555, 195, 65, 59))
        self.cell49.setCursorPosition(0)
        self.cell49.setPlaceholderText("")
        self.cell49.setObjectName("cell49")
        self.cell67 = QtWidgets.QLineEdit(self.centralwidget)
        self.cell67.setGeometry(QtCore.QRect(421, 317, 65, 59))
        self.cell67.setCursorPosition(0)
        self.cell67.setPlaceholderText("")
        self.cell67.setObjectName("cell67")
        self.cell61 = QtWidgets.QLineEdit(self.centralwidget)
        self.cell61.setGeometry(QtCore.QRect(11, 317, 65, 59))
        self.cell61.setCursorPosition(0)
        self.cell61.setPlaceholderText("")
        self.cell61.setObjectName("cell61")
        self.cell63 = QtWidgets.QLineEdit(self.centralwidget)
        self.cell63.setGeometry(QtCore.QRect(145, 317, 65, 59))
        self.cell63.setCursorPosition(0)
        self.cell63.setPlaceholderText("")
        self.cell63.setObjectName("cell63")
        self.cell43 = QtWidgets.QLineEdit(self.centralwidget)
        self.cell43.setGeometry(QtCore.QRect(145, 195, 65, 59))
        self.cell43.setCursorPosition(0)
        self.cell43.setPlaceholderText("")
        self.cell43.setObjectName("cell43")
        self.cell57 = QtWidgets.QLineEdit(self.centralwidget)
        self.cell57.setGeometry(QtCore.QRect(421, 256, 65, 59))
        self.cell57.setCursorPosition(0)
        self.cell57.setPlaceholderText("")
        self.cell57.setObjectName("cell57")
        self.cell88 = QtWidgets.QLineEdit(self.centralwidget)
        self.cell88.setGeometry(QtCore.QRect(488, 441, 65, 59))
        self.cell88.setCursorPosition(0)
        self.cell88.setPlaceholderText("")
        self.cell88.setObjectName("cell88")
        self.cell81 = QtWidgets.QLineEdit(self.centralwidget)
        self.cell81.setGeometry(QtCore.QRect(11, 441, 65, 59))
        self.cell81.setCursorPosition(0)
        self.cell81.setPlaceholderText("")
        self.cell81.setObjectName("cell81")
        self.cell71 = QtWidgets.QLineEdit(self.centralwidget)
        self.cell71.setGeometry(QtCore.QRect(11, 380, 65, 59))
        self.cell71.setCursorPosition(0)
        self.cell71.setPlaceholderText("")
        self.cell71.setObjectName("cell71")
        self.cell89 = QtWidgets.QLineEdit(self.centralwidget)
        self.cell89.setGeometry(QtCore.QRect(555, 441, 65, 59))
        self.cell89.setCursorPosition(0)
        self.cell89.setPlaceholderText("")
        self.cell89.setObjectName("cell89")
        self.cell72 = QtWidgets.QLineEdit(self.centralwidget)
        self.cell72.setGeometry(QtCore.QRect(78, 380, 65, 59))
        self.cell72.setCursorPosition(0)
        self.cell72.setPlaceholderText("")
        self.cell72.setObjectName("cell72")
        self.cell94 = QtWidgets.QLineEdit(self.centralwidget)
        self.cell94.setGeometry(QtCore.QRect(216, 502, 65, 59))
        self.cell94.setCursorPosition(0)
        self.cell94.setPlaceholderText("")
        self.cell94.setObjectName("cell94")
        self.cell86 = QtWidgets.QLineEdit(self.centralwidget)
        self.cell86.setGeometry(QtCore.QRect(350, 441, 65, 59))
        self.cell86.setCursorPosition(0)
        self.cell86.setPlaceholderText("")
        self.cell86.setObjectName("cell86")
        self.cell75 = QtWidgets.QLineEdit(self.centralwidget)
        self.cell75.setGeometry(QtCore.QRect(283, 380, 65, 59))
        self.cell75.setCursorPosition(0)
        self.cell75.setPlaceholderText("")
        self.cell75.setObjectName("cell75")
        self.cell96 = QtWidgets.QLineEdit(self.centralwidget)
        self.cell96.setGeometry(QtCore.QRect(350, 502, 65, 59))
        self.cell96.setCursorPosition(0)
        self.cell96.setPlaceholderText("")
        self.cell96.setObjectName("cell96")
        self.cell85 = QtWidgets.QLineEdit(self.centralwidget)
        self.cell85.setGeometry(QtCore.QRect(283, 441, 65, 59))
        self.cell85.setCursorPosition(0)
        self.cell85.setPlaceholderText("")
        self.cell85.setObjectName("cell85")
        self.cell73 = QtWidgets.QLineEdit(self.centralwidget)
        self.cell73.setGeometry(QtCore.QRect(145, 380, 65, 59))
        self.cell73.setCursorPosition(0)
        self.cell73.setPlaceholderText("")
        self.cell73.setObjectName("cell73")
        self.cell76 = QtWidgets.QLineEdit(self.centralwidget)
        self.cell76.setGeometry(QtCore.QRect(350, 380, 65, 59))
        self.cell76.setCursorPosition(0)
        self.cell76.setPlaceholderText("")
        self.cell76.setObjectName("cell76")
        self.cell84 = QtWidgets.QLineEdit(self.centralwidget)
        self.cell84.setGeometry(QtCore.QRect(216, 441, 65, 59))
        self.cell84.setCursorPosition(0)
        self.cell84.setPlaceholderText("")
        self.cell84.setObjectName("cell84")
        self.cell82 = QtWidgets.QLineEdit(self.centralwidget)
        self.cell82.setGeometry(QtCore.QRect(78, 441, 65, 59))
        self.cell82.setCursorPosition(0)
        self.cell82.setPlaceholderText("")
        self.cell82.setObjectName("cell82")
        self.cell99 = QtWidgets.QLineEdit(self.centralwidget)
        self.cell99.setGeometry(QtCore.QRect(555, 502, 65, 59))
        self.cell99.setCursorPosition(0)
        self.cell99.setPlaceholderText("")
        self.cell99.setObjectName("cell99")
        self.cell98 = QtWidgets.QLineEdit(self.centralwidget)
        self.cell98.setGeometry(QtCore.QRect(488, 502, 65, 59))
        self.cell98.setCursorPosition(0)
        self.cell98.setPlaceholderText("")
        self.cell98.setObjectName("cell98")
        self.cell78 = QtWidgets.QLineEdit(self.centralwidget)
        self.cell78.setGeometry(QtCore.QRect(488, 380, 65, 59))
        self.cell78.setCursorPosition(0)
        self.cell78.setPlaceholderText("")
        self.cell78.setObjectName("cell78")
        self.cell77 = QtWidgets.QLineEdit(self.centralwidget)
        self.cell77.setGeometry(QtCore.QRect(421, 380, 65, 59))
        self.cell77.setCursorPosition(0)
        self.cell77.setPlaceholderText("")
        self.cell77.setObjectName("cell77")
        self.cell95 = QtWidgets.QLineEdit(self.centralwidget)
        self.cell95.setGeometry(QtCore.QRect(283, 502, 65, 59))
        self.cell95.setCursorPosition(0)
        self.cell95.setPlaceholderText("")
        self.cell95.setObjectName("cell95")
        self.cell87 = QtWidgets.QLineEdit(self.centralwidget)
        self.cell87.setGeometry(QtCore.QRect(421, 441, 65, 59))
        self.cell87.setCursorPosition(0)
        self.cell87.setPlaceholderText("")
        self.cell87.setObjectName("cell87")
        self.cell93 = QtWidgets.QLineEdit(self.centralwidget)
        self.cell93.setGeometry(QtCore.QRect(145, 502, 65, 59))
        self.cell93.setCursorPosition(0)
        self.cell93.setPlaceholderText("")
        self.cell93.setObjectName("cell93")
        self.cell91 = QtWidgets.QLineEdit(self.centralwidget)
        self.cell91.setGeometry(QtCore.QRect(11, 502, 65, 59))
        self.cell91.setCursorPosition(0)
        self.cell91.setPlaceholderText("")
        self.cell91.setObjectName("cell91")
        self.cell74 = QtWidgets.QLineEdit(self.centralwidget)
        self.cell74.setGeometry(QtCore.QRect(216, 380, 65, 59))
        self.cell74.setCursorPosition(0)
        self.cell74.setPlaceholderText("")
        self.cell74.setObjectName("cell74")
        self.cell79 = QtWidgets.QLineEdit(self.centralwidget)
        self.cell79.setGeometry(QtCore.QRect(555, 380, 65, 59))
        self.cell79.setCursorPosition(0)
        self.cell79.setPlaceholderText("")
        self.cell79.setObjectName("cell79")
        self.cell83 = QtWidgets.QLineEdit(self.centralwidget)
        self.cell83.setGeometry(QtCore.QRect(145, 441, 65, 59))
        self.cell83.setCursorPosition(0)
        self.cell83.setPlaceholderText("")
        self.cell83.setObjectName("cell83")
        self.cell92 = QtWidgets.QLineEdit(self.centralwidget)
        self.cell92.setGeometry(QtCore.QRect(78, 502, 65, 59))
        self.cell92.setCursorPosition(0)
        self.cell92.setPlaceholderText("")
        self.cell92.setObjectName("cell92")
        self.cell97 = QtWidgets.QLineEdit(self.centralwidget)
        self.cell97.setGeometry(QtCore.QRect(421, 502, 65, 59))
        self.cell97.setCursorPosition(0)
        self.cell97.setPlaceholderText("")
        self.cell97.setObjectName("cell97")
        MainWindow.setCentralWidget(self.centralwidget)
        self.actionFile = QtWidgets.QAction(MainWindow)
        self.actionFile.setObjectName("actionFile")
        self.actionNew = QtWidgets.QAction(MainWindow)
        self.actionNew.setObjectName("actionNew")
        self.actionSave = QtWidgets.QAction(MainWindow)
        self.actionSave.setObjectName("actionSave")
        self.actionEdit = QtWidgets.QAction(MainWindow)
        self.actionEdit.setObjectName("actionEdit")
        self.actionCopy = QtWidgets.QAction(MainWindow)
        self.actionCopy.setObjectName("actionCopy")
        self.actionPaste = QtWidgets.QAction(MainWindow)
        self.actionPaste.setObjectName("actionPaste")

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.solve_button.setText(_translate("MainWindow", "Solve"))
        self.clear_button.setText(_translate("MainWindow", "Clear"))
        self.actionFile.setText(_translate("MainWindow", "File"))
        self.actionNew.setText(_translate("MainWindow", "New"))
        self.actionNew.setStatusTip(_translate("MainWindow", "Create a new file"))
        self.actionNew.setShortcut(_translate("MainWindow", "Ctrl+N"))
        self.actionSave.setText(_translate("MainWindow", "Save"))
        self.actionSave.setStatusTip(_translate("MainWindow", "Save a file"))
        self.actionEdit.setText(_translate("MainWindow", "Edit"))
        self.actionCopy.setText(_translate("MainWindow", "Copy"))
        self.actionCopy.setStatusTip(_translate("MainWindow", "Copy a file"))
        self.actionPaste.setText(_translate("MainWindow", "Paste"))
        self.actionPaste.setStatusTip(_translate("MainWindow", "Paste a file"))
        self.actionPaste.setShortcut(_translate("MainWindow", "Ctrl+V"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

