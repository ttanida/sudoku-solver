from PyQt5 import QtCore, QtGui, QtWidgets
import numpy as np


class UiMainWindow(object):
    def setup_ui(self, main_window):
        main_window.setObjectName("MainWindow")
        main_window.setFixedSize(631, 646)

        font = QtGui.QFont()
        font.setPointSize(24)
        main_window.setFont(font)
        main_window.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))

        self.centralwidget = QtWidgets.QWidget(main_window)
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

        # positional settings of row and column cells
        self.column_geometry_settings = [11, 78, 145, 216, 283, 350, 421, 488, 555]
        self.row_geometry_settings = [11, 71, 132, 195, 256, 317, 380, 441, 502]

        # setting up all 81 (9x9) cells in sudoku grid
        for row in range(1, 10):
            for column in range(1, 10):
                exec(f'self.cell{row}{column} = QtWidgets.QLineEdit(self.centralwidget)', {"self": self, "QtWidgets": QtWidgets})
                eval(f'self.cell{row}{column}.setGeometry(QtCore.QRect({self.column_geometry_settings[column-1]}, '
                     f'{self.row_geometry_settings[row-1]}, 65, 59))',{"self": self, "QtCore": QtCore})
                eval(f'self.cell{row}{column}.setCursorPosition(0)', {"self": self})
                eval(f'self.cell{row}{column}.setPlaceholderText("")', {"self": self})
                eval(f'self.cell{row}{column}.setObjectName("cell{row}{column}")', {"self": self})
                eval(f'self.cell{row}{column}.setValidator(self.validator)', {"self": self})
                eval(f'self.cell{row}{column}.setFont(cell_font)', {"self": self, "cell_font": cell_font})
                eval(f'self.cell{row}{column}.setAlignment(QtCore.Qt.AlignCenter)', {"self": self, "QtCore": QtCore})
                eval(f'self.cell{row}{column}.textChanged.connect(self.check_constraints)', {"self": self})

        main_window.setCentralWidget(self.centralwidget)

        self.retranslate_ui(main_window)
        QtCore.QMetaObject.connectSlotsByName(main_window)

    def retranslate_ui(self, main_window):
        _translate = QtCore.QCoreApplication.translate
        main_window.setWindowTitle(_translate("MainWindow", "Sudoku solver"))
        self.solve_button.setText(_translate("MainWindow", "Solve"))
        self.clear_button.setText(_translate("MainWindow", "Clear"))

    def check_constraints_rows_columns(self, values_of_cells):
        """Checks if initial user input (matrix values_of_cells) satisfies the row/column sudoku constraints
        (i.e. no duplicate number in same row/column)

        If normal matrix values_of_cells is passed as input, the method checks for the row constraints.
        If transposed matrix values_of_cells is passed as input, the method checks for the column constraints.

        Method goes row-by-row (or column-by-column if transposed matrix passed as argument) and stores values != 0
        in dictionary "found_values" with the values as keys and the respective column (or row) as values.

        If there is a duplicate value in a row, it returns a tuple of (row, column1, column2), where column1 is the
        column of the 1st duplicate value and column2 is the column of the 2nd duplicate value.

        Similarly, if transposed matrix is passed as argument and there is a duplicate value in a column, it returns
        a tuple of (column, row1, row2), where row1 is the row of the 1st duplicate value and row2 is the row of the
        2nd duplicate value.

        If there are no duplicate values, method return None.
        """
        for row in range(1, 10):
            found_values = {}
            for column in range(1, 10):
                value_of_cell = values_of_cells[row - 1, column - 1]
                if value_of_cell != 0:
                    if value_of_cell not in found_values.keys():
                        found_values[value_of_cell] = column
                    else:
                        return row, found_values[value_of_cell], column

        return None

    def change_row_color(self, check_rows):
        if check_rows is not None:
            for column in range(1,10):
                eval(f'self.cell{check_rows[0]}{column}.setStyleSheet("background-color: rgb(255, 128, 128);")', {"self": self})

            eval(f'self.cell{check_rows[0]}{check_rows[1]}.setStyleSheet("background-color: rgb(230, 0, 0);")', {"self": self})
            eval(f'self.cell{check_rows[0]}{check_rows[2]}.setStyleSheet("background-color: rgb(230, 0, 0);")', {"self": self})

    def change_column_color(self, check_columns):
        if check_columns is not None:
            for row in range(1,10):
                eval(f'self.cell{row}{check_columns[0]}.setStyleSheet("background-color: rgb(255, 128, 128);")', {"self": self})

            eval(f'self.cell{check_columns[0]}{check_columns[1]}.setStyleSheet("background-color: rgb(230, 0, 0);")', {"self": self})
            eval(f'self.cell{check_columns[0]}{check_columns[2]}.setStyleSheet("background-color: rgb(230, 0, 0);")', {"self": self})

    def retrieve_values_of_cells(self):
        values_of_cells = np.zeros([9, 9])
        for row in range(1, 10):
            for column in range(1, 10):
                value_of_cell = eval(f'self.cell{row}{column}.text()', {"self": self})
                if value_of_cell != "":
                    values_of_cells[row - 1, column - 1] = int(value_of_cell)

        return values_of_cells

    def check_constraints(self):
        """Checks if initial user input satisfies the sudoku constraints (e.g. no duplicate number in same row)

        Any time a cell value is modified, check_constraints calls method retrieve_values_of_cells to retrieve
        all 81 cells values and store them in a 9x9 numpy array values_of_cells.

        If a cell is empty, its value is stored as a zero.

        Check_constraints then passes values_of_cells and values_of_cells transposed into method
        check_constraints_rows_columns to check if the row and column constraints are not violated.

        If a constraint is violated, the respective row/column and cells are highlighted in red by
        methods change_row_color and change_column_color.
        """

        values_of_cells = self.retrieve_values_of_cells()

        # check for duplicates in rows
        check_rows = self.check_constraints_rows_columns(values_of_cells)
        self.change_row_color(check_rows)

        # check for duplicates in columns (values_of_cells passed as transpose)
        check_columns = self.check_constraints_rows_columns(values_of_cells.T)
        self.change_column_color(check_columns)







