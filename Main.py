import sys
import PyQt5.QtWidgets as QtWidgets
from MaTyTuWindow import Window


def run():
    app = QtWidgets.QApplication(sys.argv)
    gui = Window()
    sys.exit(app.exec_())

if __name__ == "__main__":
    run()
