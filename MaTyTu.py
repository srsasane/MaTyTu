# -*- coding: utf-8 -*-
"""
Created on Thu Apr 16 07:48:25 2020

@author: Sudhir Sasane
Comments,Critics Suggestion to srsasane@protonmail.com
5th Tutorial : https://www.youtube.com/watch?v=ZKYr9DB-Pzc
"""

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

__version__ = 'β'
__author__ = 'Sudhir Sasane(सुधिर ससाणे)'
word_count = 10
DURATION_INT = 10
button_font = QFont("Aksharyogini2", 14, QFont.Bold)
title_font = QFont("Aksharyogini2", 24, QFont.Bold)
normal_font = QFont("Aksharyogini2", 22, QFont.Bold)
marathi_font = QFont("Aksharyogini2", 32, QFont.Bold)


class Window(QMainWindow):

    def __init__(self, parent=None):
        super(Window, self).__init__(parent)

        centralWidget = QWidget()
        self.setCentralWidget(centralWidget)
        self.grid = QGridLayout(centralWidget)

        V = QApplication.desktop().screenGeometry()
        h = V.height()
        w = V.width()
        self.AppWidth = 800
        self.AppHeight = 500
        self.setGeometry(h / 4, w / 20, self.AppWidth, self.AppHeight)
        # self.setFixedSize(x, y)
        self.setWindowTitle('MaTyTu β')
        self.setWindowIcon(QIcon('python.png'))
        self.filename = 'level1.txt'
        self.home()

    def home(self):

        self.load_words()
        self.load_matytu()
        self.show()

    def load_matytu(self):

        ##
        toolbarBox = QToolBar(self)
        toolbarBox.setFixedWidth(self.AppWidth)

        self.addToolBar(Qt.TopToolBarArea, toolbarBox)

        l1_button = QRadioButton(self, text="पातळी१", checkable=True)
        l1_button.setChecked(True)
        l1_button.clicked.connect(self.level1)
        l2_button = QRadioButton(self, text="पातळी२", checkable=True)
        l2_button.clicked.connect(self.level2)
        l3_button = QRadioButton(self, text="पातळी३", checkable=True)
        l3_button.clicked.connect(self.level3)
        l4_button = QRadioButton(self, text="पातळी४", checkable=True)
        l4_button.clicked.connect(self.level4)
        l5_button = QRadioButton(self, text="पातळी५", checkable=True)
        l5_button.clicked.connect(self.level5)
        ab_button = QToolButton(self, text="About", checkable=True)
        ab_button.clicked.connect(self.about_app)
        q_button = QPushButton(self, text='&Quit')
        q_button.clicked.connect(self.close_application)
        q_button.setShortcut('Ctrl+Q')
        q_button.setToolTip('Ctrl+Q')

        k_button = QPushButton(self)
        k_button.setIcon(QIcon('Keyboard.png'))
        k_button.setToolTip('F8')
        k_button.clicked.connect(self.show_keyboard)
        self.dialog = KeyboardLayoutWindow(self)
        group = QButtonGroup(self, exclusive=True)

        for button in (l1_button, l2_button, l3_button, l4_button, l5_button,
                       ab_button, q_button, k_button):
            toolbarBox.addWidget(button)
            button.setFont(button_font)
            group.addButton(button)

        self.groupBox = QGroupBox('म टाय ट्यु-β')
        self.groupBox.setFont(title_font)
        self.groupBox.move(150, 50)
        self.groupBox.resize(400, 400)

        vBox = QVBoxLayout()
        self.word_label = QLabel('', self)
        self.get_word()
        self.word_label.setAlignment(Qt.AlignCenter)
        self.word_label.setFont(marathi_font)
        self.word_label.setStyleSheet("QLabel { background-color : Blue; color : white; }");

        vBox.addWidget(self.word_label)

        self.time_label = QLabel('शेवटच्या शब्दाला लागलेला वेळ:-', self)
        self.time_label.setAlignment(Qt.AlignCenter)
        self.time_label.setStyleSheet("QLabel { background-color : gray; color :black; }");
        self.time_label.setFont(normal_font)
        vBox.addWidget(self.time_label)
        self.groupBox.setLayout(vBox)
        self.entry = QLineEdit("येथे टाईप करा...", self)

        self.entry.setFont(marathi_font)
        vBox.addWidget(self.entry)

        self.start_time = time.time()

        self.grid.addWidget(self.groupBox)
        self.grid.addWidget(self.createStatsGroup())
    def keyPressEvent(self, event):
        key = event.key()
        # Show keyboard Layout if key F8 is pressed.
        if key == Qt.Key_F8:
            self.show_keyboard()
            self.dialog = KeyboardLayoutWindow(self)

        if key == Qt.Key_Return:
            print(self.entry.text())
            if self.entry.text() == self.words[self.word_id]:
                self.end_time = time.time()
                time_taken = float(self.end_time - self.start_time)
                print("time taken: " + str(time_taken))

                self.entry.clear()
                self.start_time = self.end_time
                self.time_label.setStyleSheet("QLabel { background-color : gray; color :black; }");
                self.time_label.setText("शेवटचा शब्द:-  ' " + self.word + " ' \nलागलेला वेळ: %.3f Sec" % (time_taken))
                self.get_word()


            else:
                self.entry.clear()
                self.end_time = time.time()

                self.time_label.setStyleSheet("QLabel { background-color : red; color :black; }");
                self.time_label.setText("शेवटचा शब्द: ' " + self.word + " ' चुकला.")
                self.get_word()

                self.start_time = self.end_time

    def level1(self):
        self.filename = 'level1.txt'
        self.load_words()
        QMessageBox.about(self, 'Level Select', "<P><font size = 6><b>पातळी १ निवडली आहे.</b>")
        self.get_word()

    def level2(self):

        self.filename = 'level2.txt'
        self.load_words()
        QMessageBox.about(self, 'Level Select', "<P><font size = 6><b>पातळी २ निवडली आहे.</b>")
        self.get_word()
        print("Words from '" + self.filename + "' loaded successfully")

    def level3(self):

        self.filename = 'level3.txt'
        self.load_words()
        QMessageBox.about(self, 'Level Select', "<P><font size = 6><b>पातळी ३ निवडली आहे.</b>")
        self.get_word()
        print("Words from '" + self.filename + "' loaded successfully")

    def level4(self):
        print('I am in Level 4 now')
        self.filename = 'level4.txt'
        self.load_words()
        QMessageBox.about(self, 'Level Select', "<P><font size = 6><b>पातळी ४ निवडली आहे.</b>")
        self.get_word()
        print("Words from '" + self.filename + "' loaded successfully")

    def level5(self):
        print('I am in Level 5 now')
        self.filename = 'MarathiWords.txt'
        self.load_words()
        QMessageBox.about(self, 'Level Select', "<P><font size = 6><b>पातळी ५ निवडली आहे.</b>")
        self.get_word()
        print("Words from '" + self.filename + "' loaded successfully")

    def show_keyboard(self):

        self.dialog.show()

    def font_choice(self):
        font, valid = QFontDialog.getFont()
        if valid:
            self.styleChoice.setFont(font)

    def style_choice(self, text):

        self.styleChoice.setText(text)
        QApplication.setStyle(QStyleFactory.create(text))

    def close_application(self):
        choice = QMessageBox.question(self, 'MaTyTu',
                                      "<P><font size = 6><b>मटायट्यु <FONT COLOR='#800000'>बंद</FONT> करा ?</b> ",
                                      QMessageBox.Yes | QMessageBox.No)

        if choice == QMessageBox.Yes:
            print("Exiting Now!!!")
            sys.exit()


        else:
            pass

    def about_app(self):

        qmsgBox = QMessageBox(self)
        qmsgBox.setStyleSheet(
            'QMessageBox {background-color: #2b5b84; color: white;}\nQPushButton{color: white; font-size: 18px; background-color: #1d1d1d; border-radius: 10px; padding: 10px; text-align: center;}\n QPushButton:hover{color: #2b5b84;}')
        QMessageBox.about(qmsgBox, 'म टाय ट्यु',
                          """<font color='white'><font size=6><p><b>Marathi Typing Tutor</b></p></font>
            <font size=4><p><b>Version:</b> {0}</p>
            <p><b>Author:  {1}</b></p>
            <p><b>Web:</b></font><a href='https://vidnyankendra.org/'><font color='black'><font size=5>Vidnyan Kendra (विज्ञान केंद्र)</font></a></p>
            <font color='white'><font size=4><p><b>Email: </b>srsasane@protonmail.com</p>
            <p><b>Copyright:</b>  &copy; 2020 MaTyTu Project Contributors and Others.
            <p><b>Distribution:</b> <a href='https://www.gnu.org/licenses/gpl-3.0.en.html'><font color='black'>The GNU General Public License v3.0</font></a></p>
            <p>This application can be used to learn Marathi Typing (Unicode Fonts).</p>
            <p><b>You are using:</b></p>
            <p>Python {2} - Qt {3} - PyQt {4} on {5}</p></font>""".format(
                              __version__, __author__, platform.python_version(),
                              QT_VERSION_STR, PYQT_VERSION_STR, platform.system()))

    def load_words(self):
        self.words = []
        f = open(self.filename, 'r', encoding="utf-8")
        for line in f:
            self.words.append(line.strip())
            random.shuffle(self.words)
        print(len(self.words) - 1, ' words from file ' + self.filename + ' loaded successfuly.')

    def get_word(self):
        self.word_id = random.randint(0, len(self.words) - 1)
        self.word = self.words[self.word_id]
        self.word_label.setText(self.word)

    def createStatsGroup(self):

        groupBox1 = QGroupBox("Typing Statistics")
        groupBox1.setFont(title_font)

        time_label = QLabel("Time")
        time_label.setFont(normal_font)
        wpm_label = QLabel("WPM")
        wpm_label.setFont(normal_font)
        acr_label = QLabel("Accuracy")
        acr_label.setFont(normal_font)

        hbox = QHBoxLayout()
        hbox.addWidget(time_label)
        hbox.addWidget(wpm_label)
        hbox.addWidget(acr_label)
        # hbox.addStretch(1)
        groupBox1.setLayout(hbox)
        return groupBox1


class KeyboardLayoutWindow(QMainWindow):
    def __init__(self, parent=None):
        super(KeyboardLayoutWindow, self).__init__(parent)
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


def run():
    app = QApplication(sys.argv)

    GUI = Window()
    sys.exit(app.exec_())


run()
