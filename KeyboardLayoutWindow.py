import platform
import random
import sys
import time

from PyQt5.QtCore import Qt, QT_VERSION_STR, PYQT_VERSION_STR
from PyQt5.QtGui import *
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtWidgets import (QApplication, QGridLayout, QGroupBox, QLabel, QStyleFactory, QButtonGroup,
                             QVBoxLayout, QLineEdit, QFontDialog, QMessageBox, QWidget, QMainWindow,
                             QToolBar, QPushButton, QRadioButton, QToolButton, QHBoxLayout)

# import PyQt5.QtCore as QtCore
# import PyQt5.QtGui as QtGui
import PyQt5.QtWidgets as QtWidgets



class KeyboardLayoutWindow(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(KeyboardLayoutWindow, self).__init__(parent)
        # ... (rest of the code remains the same)
        self.setWindowTitle("Keyboard Layout")

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        lay = QVBoxLayout(self.central_widget)

        label = QLabel(self)
        pixmap = QPixmap('kbdlayout.jpg')
        pixmap = pixmap.scaled(760, 600, Qt.KeepAspectRatio)
        label.setPixmap(pixmap)
        self.resize(pixmap.width(), pixmap.height())

        lay.addWidget(label)

