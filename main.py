import sys

from PySide2 import QtWidgets


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    label = QtWidgets.QLabel("<font color=red size=40>Hello World!</font>")
    label.show()
    app.exec_()
