#!/usr/bin/env python

from PyQt5 import QtWidgets
from ui_main_window import UiMainWindow

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()

    # sets up the UiMainWindow object that entails the suduko field
    ui = UiMainWindow()
    ui.setup_ui(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

