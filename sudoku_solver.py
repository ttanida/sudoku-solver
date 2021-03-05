# -*- coding: utf-8 -*-
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setup_ui(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setFixedSize(631, 646)

        font = QtGui.QFont()
        font.setPointSize(24)
        MainWindow.setFont(font)
        MainWindow.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        # sudoku_field
        self.sudoku_field = QtWidgets.QLabel(self.centralwidget)
        self.sudoku_field.setGeometry(QtCore.QRect(0, 0, 631, 571))
        self.sudoku_field.setText("")
        self.sudoku_field.setPixmap(QtGui.QPixmap("sudoku-blankgrid.png"))
        self.sudoku_field.setScaledContents(True)
        self.sudoku_field.setObjectName("sudoku_field")

        # solve_button
        self.solve_button = QtWidgets.QPushButton(self.centralwidget)
        self.solve_button.setGeometry(QtCore.QRect(110, 580, 181, 61))
        self.solve_button.setObjectName("solve_button")

        # clear_button
        self.clear_button = QtWidgets.QPushButton(self.centralwidget)
        self.clear_button.setGeometry(QtCore.QRect(340, 580, 191, 61))
        self.clear_button.setFont(font)
        self.clear_button.setObjectName("clear_button")

        # validator to ensure only one integer between 1 - 9 is entered into cells
        rx = QtCore.QRegExp("[1-9]{1}")
        self.validator = QtGui.QRegExpValidator(rx)

        # font_size of cells
        cell_font = QtGui.QFont()
        cell_font.setPointSize(40)

        # cells row 1
        self.cell11 = QtWidgets.QLineEdit(self.centralwidget)
        self.cell11.setGeometry(QtCore.QRect(11, 11, 65, 59))
        self.cell12 = QtWidgets.QLineEdit(self.centralwidget)
        self.cell12.setGeometry(QtCore.QRect(78, 11, 65, 59))
        self.cell13 = QtWidgets.QLineEdit(self.centralwidget)
        self.cell13.setGeometry(QtCore.QRect(145, 11, 65, 59))
        self.cell14 = QtWidgets.QLineEdit(self.centralwidget)
        self.cell14.setGeometry(QtCore.QRect(216, 11, 65, 59))
        self.cell15 = QtWidgets.QLineEdit(self.centralwidget)
        self.cell15.setGeometry(QtCore.QRect(283, 11, 65, 59))
        self.cell16 = QtWidgets.QLineEdit(self.centralwidget)
        self.cell16.setGeometry(QtCore.QRect(350, 11, 65, 59))
        self.cell17 = QtWidgets.QLineEdit(self.centralwidget)
        self.cell17.setGeometry(QtCore.QRect(421, 11, 65, 59))
        self.cell18 = QtWidgets.QLineEdit(self.centralwidget)
        self.cell18.setGeometry(QtCore.QRect(488, 11, 65, 59))
        self.cell19 = QtWidgets.QLineEdit(self.centralwidget)
        self.cell19.setGeometry(QtCore.QRect(555, 11, 65, 59))

        # cells row 2
        self.cell21 = QtWidgets.QLineEdit(self.centralwidget)
        self.cell21.setGeometry(QtCore.QRect(11, 71, 65, 59))
        self.cell22 = QtWidgets.QLineEdit(self.centralwidget)
        self.cell22.setGeometry(QtCore.QRect(78, 71, 65, 59))
        self.cell23 = QtWidgets.QLineEdit(self.centralwidget)
        self.cell23.setGeometry(QtCore.QRect(145, 71, 65, 59))
        self.cell24 = QtWidgets.QLineEdit(self.centralwidget)
        self.cell24.setGeometry(QtCore.QRect(216, 71, 65, 59))
        self.cell25 = QtWidgets.QLineEdit(self.centralwidget)
        self.cell25.setGeometry(QtCore.QRect(283, 71, 65, 59))
        self.cell26 = QtWidgets.QLineEdit(self.centralwidget)
        self.cell26.setGeometry(QtCore.QRect(350, 71, 65, 59))
        self.cell27 = QtWidgets.QLineEdit(self.centralwidget)
        self.cell27.setGeometry(QtCore.QRect(421, 71, 65, 59))
        self.cell28 = QtWidgets.QLineEdit(self.centralwidget)
        self.cell28.setGeometry(QtCore.QRect(488, 71, 65, 59))
        self.cell29 = QtWidgets.QLineEdit(self.centralwidget)
        self.cell29.setGeometry(QtCore.QRect(555, 71, 65, 59))

        # cells row 3
        self.cell31 = QtWidgets.QLineEdit(self.centralwidget)
        self.cell31.setGeometry(QtCore.QRect(11, 132, 65, 59))
        self.cell32 = QtWidgets.QLineEdit(self.centralwidget)
        self.cell32.setGeometry(QtCore.QRect(78, 132, 65, 59))
        self.cell33 = QtWidgets.QLineEdit(self.centralwidget)
        self.cell33.setGeometry(QtCore.QRect(145, 132, 65, 59))
        self.cell34 = QtWidgets.QLineEdit(self.centralwidget)
        self.cell34.setGeometry(QtCore.QRect(216, 132, 65, 59))
        self.cell35 = QtWidgets.QLineEdit(self.centralwidget)
        self.cell35.setGeometry(QtCore.QRect(283, 132, 65, 59))
        self.cell36 = QtWidgets.QLineEdit(self.centralwidget)
        self.cell36.setGeometry(QtCore.QRect(350, 132, 65, 59))
        self.cell37 = QtWidgets.QLineEdit(self.centralwidget)
        self.cell37.setGeometry(QtCore.QRect(421, 132, 65, 59))
        self.cell38 = QtWidgets.QLineEdit(self.centralwidget)
        self.cell38.setGeometry(QtCore.QRect(488, 132, 65, 59))
        self.cell39 = QtWidgets.QLineEdit(self.centralwidget)
        self.cell39.setGeometry(QtCore.QRect(555, 132, 65, 59))
        # cells row 4
        self.cell41 = QtWidgets.QLineEdit(self.centralwidget)
        self.cell41.setGeometry(QtCore.QRect(11, 195, 65, 59))
        self.cell42 = QtWidgets.QLineEdit(self.centralwidget)
        self.cell42.setGeometry(QtCore.QRect(78, 195, 65, 59))
        self.cell43 = QtWidgets.QLineEdit(self.centralwidget)
        self.cell43.setGeometry(QtCore.QRect(145, 195, 65, 59))
        self.cell44 = QtWidgets.QLineEdit(self.centralwidget)
        self.cell44.setGeometry(QtCore.QRect(216, 195, 65, 59))
        self.cell45 = QtWidgets.QLineEdit(self.centralwidget)
        self.cell45.setGeometry(QtCore.QRect(283, 195, 65, 59))
        self.cell46 = QtWidgets.QLineEdit(self.centralwidget)
        self.cell46.setGeometry(QtCore.QRect(350, 195, 65, 59))
        self.cell47 = QtWidgets.QLineEdit(self.centralwidget)
        self.cell47.setGeometry(QtCore.QRect(421, 195, 65, 59))
        self.cell48 = QtWidgets.QLineEdit(self.centralwidget)
        self.cell48.setGeometry(QtCore.QRect(488, 195, 65, 59))
        self.cell49 = QtWidgets.QLineEdit(self.centralwidget)
        self.cell49.setGeometry(QtCore.QRect(555, 195, 65, 59))

        # cells row 5
        self.cell51 = QtWidgets.QLineEdit(self.centralwidget)
        self.cell51.setGeometry(QtCore.QRect(11, 256, 65, 59))
        self.cell52 = QtWidgets.QLineEdit(self.centralwidget)
        self.cell52.setGeometry(QtCore.QRect(78, 256, 65, 59))
        self.cell53 = QtWidgets.QLineEdit(self.centralwidget)
        self.cell53.setGeometry(QtCore.QRect(145, 256, 65, 59))
        self.cell54 = QtWidgets.QLineEdit(self.centralwidget)
        self.cell54.setGeometry(QtCore.QRect(216, 256, 65, 59))
        self.cell55 = QtWidgets.QLineEdit(self.centralwidget)
        self.cell55.setGeometry(QtCore.QRect(283, 256, 65, 59))
        self.cell56 = QtWidgets.QLineEdit(self.centralwidget)
        self.cell56.setGeometry(QtCore.QRect(350, 256, 65, 59))
        self.cell57 = QtWidgets.QLineEdit(self.centralwidget)
        self.cell57.setGeometry(QtCore.QRect(421, 256, 65, 59))
        self.cell58 = QtWidgets.QLineEdit(self.centralwidget)
        self.cell58.setGeometry(QtCore.QRect(488, 256, 65, 59))
        self.cell59 = QtWidgets.QLineEdit(self.centralwidget)
        self.cell59.setGeometry(QtCore.QRect(555, 256, 65, 59))

        # cells row 6
        self.cell61 = QtWidgets.QLineEdit(self.centralwidget)
        self.cell61.setGeometry(QtCore.QRect(11, 317, 65, 59))
        self.cell62 = QtWidgets.QLineEdit(self.centralwidget)
        self.cell62.setGeometry(QtCore.QRect(78, 317, 65, 59))
        self.cell63 = QtWidgets.QLineEdit(self.centralwidget)
        self.cell63.setGeometry(QtCore.QRect(145, 317, 65, 59))
        self.cell64 = QtWidgets.QLineEdit(self.centralwidget)
        self.cell64.setGeometry(QtCore.QRect(216, 317, 65, 59))
        self.cell65 = QtWidgets.QLineEdit(self.centralwidget)
        self.cell65.setGeometry(QtCore.QRect(283, 317, 65, 59))
        self.cell66 = QtWidgets.QLineEdit(self.centralwidget)
        self.cell66.setGeometry(QtCore.QRect(350, 317, 65, 59))
        self.cell67 = QtWidgets.QLineEdit(self.centralwidget)
        self.cell67.setGeometry(QtCore.QRect(421, 317, 65, 59))
        self.cell68 = QtWidgets.QLineEdit(self.centralwidget)
        self.cell68.setGeometry(QtCore.QRect(488, 317, 65, 59))
        self.cell69 = QtWidgets.QLineEdit(self.centralwidget)
        self.cell69.setGeometry(QtCore.QRect(555, 317, 65, 59))

        # cells row 7
        self.cell71 = QtWidgets.QLineEdit(self.centralwidget)
        self.cell71.setGeometry(QtCore.QRect(11, 380, 65, 59))
        self.cell72 = QtWidgets.QLineEdit(self.centralwidget)
        self.cell72.setGeometry(QtCore.QRect(78, 380, 65, 59))
        self.cell73 = QtWidgets.QLineEdit(self.centralwidget)
        self.cell73.setGeometry(QtCore.QRect(145, 380, 65, 59))
        self.cell74 = QtWidgets.QLineEdit(self.centralwidget)
        self.cell74.setGeometry(QtCore.QRect(216, 380, 65, 59))
        self.cell75 = QtWidgets.QLineEdit(self.centralwidget)
        self.cell75.setGeometry(QtCore.QRect(283, 380, 65, 59))
        self.cell76 = QtWidgets.QLineEdit(self.centralwidget)
        self.cell76.setGeometry(QtCore.QRect(350, 380, 65, 59))
        self.cell77 = QtWidgets.QLineEdit(self.centralwidget)
        self.cell77.setGeometry(QtCore.QRect(421, 380, 65, 59))
        self.cell78 = QtWidgets.QLineEdit(self.centralwidget)
        self.cell78.setGeometry(QtCore.QRect(488, 380, 65, 59))
        self.cell79 = QtWidgets.QLineEdit(self.centralwidget)
        self.cell79.setGeometry(QtCore.QRect(555, 380, 65, 59))

        # cells row 8
        self.cell81 = QtWidgets.QLineEdit(self.centralwidget)
        self.cell81.setGeometry(QtCore.QRect(11, 441, 65, 59))
        self.cell82 = QtWidgets.QLineEdit(self.centralwidget)
        self.cell82.setGeometry(QtCore.QRect(78, 441, 65, 59))
        self.cell83 = QtWidgets.QLineEdit(self.centralwidget)
        self.cell83.setGeometry(QtCore.QRect(145, 441, 65, 59))
        self.cell84 = QtWidgets.QLineEdit(self.centralwidget)
        self.cell84.setGeometry(QtCore.QRect(216, 441, 65, 59))
        self.cell85 = QtWidgets.QLineEdit(self.centralwidget)
        self.cell85.setGeometry(QtCore.QRect(283, 441, 65, 59))
        self.cell86 = QtWidgets.QLineEdit(self.centralwidget)
        self.cell86.setGeometry(QtCore.QRect(350, 441, 65, 59))
        self.cell87 = QtWidgets.QLineEdit(self.centralwidget)
        self.cell87.setGeometry(QtCore.QRect(421, 441, 65, 59))
        self.cell88 = QtWidgets.QLineEdit(self.centralwidget)
        self.cell88.setGeometry(QtCore.QRect(488, 441, 65, 59))
        self.cell89 = QtWidgets.QLineEdit(self.centralwidget)
        self.cell89.setGeometry(QtCore.QRect(555, 441, 65, 59))

        # cells row 9
        self.cell91 = QtWidgets.QLineEdit(self.centralwidget)
        self.cell91.setGeometry(QtCore.QRect(11, 502, 65, 59))
        self.cell92 = QtWidgets.QLineEdit(self.centralwidget)
        self.cell92.setGeometry(QtCore.QRect(78, 502, 65, 59))
        self.cell93 = QtWidgets.QLineEdit(self.centralwidget)
        self.cell93.setGeometry(QtCore.QRect(145, 502, 65, 59))
        self.cell94 = QtWidgets.QLineEdit(self.centralwidget)
        self.cell94.setGeometry(QtCore.QRect(216, 502, 65, 59))
        self.cell95 = QtWidgets.QLineEdit(self.centralwidget)
        self.cell95.setGeometry(QtCore.QRect(283, 502, 65, 59))
        self.cell96 = QtWidgets.QLineEdit(self.centralwidget)
        self.cell96.setGeometry(QtCore.QRect(350, 502, 65, 59))
        self.cell97 = QtWidgets.QLineEdit(self.centralwidget)
        self.cell97.setGeometry(QtCore.QRect(421, 502, 65, 59))
        self.cell98 = QtWidgets.QLineEdit(self.centralwidget)
        self.cell98.setGeometry(QtCore.QRect(488, 502, 65, 59))
        self.cell99 = QtWidgets.QLineEdit(self.centralwidget)
        self.cell99.setGeometry(QtCore.QRect(555, 502, 65, 59))

        for row in range(1, 10):
            for column in range(1,10):
                eval(f'self.cell{row}{column}.setCursorPosition(0)', {"self": self})
                eval(f'self.cell{row}{column}.setPlaceholderText("")', {"self": self})
                eval(f'self.cell{row}{column}.setObjectName("cell{row}{column}")', {"self": self})
                eval(f'self.cell{row}{column}.setValidator(self.validator)', {"self": self})
                eval(f'self.cell{row}{column}.setFont(cell_font)', {"self": self, "cell_font": cell_font})
                eval(f'self.cell{row}{column}.setAlignment(QtCore.Qt.AlignCenter)', {"self": self, "QtCore": QtCore})
                eval(f'self.cell{row}{column}.textChanged.connect(self.check_constraints)', {"self": self})

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Sudoku solver"))
        self.solve_button.setText(_translate("MainWindow", "Solve"))
        self.clear_button.setText(_translate("MainWindow", "Clear"))

    # every time the input in any cell is modified, method "check_constraints" checks whether the sudoku constraints
    # are still fulfilled (e.g. only one number between 1-9 in each row and column)
    def check_constraints(self):
        values_of_cells = []
        for row in range(1, 10):
            values_of_cells.append([eval(f'self.cell{row}{column}.text()', {"self": self}) for column in range(1, 10)])

        for row in values_of_cells:
            print(row)
        print()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setup_ui(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

