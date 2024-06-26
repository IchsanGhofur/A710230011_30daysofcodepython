from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys

class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Aplikasi Timer")
        self.setGeometry(100, 100, 400, 600)
        self.UiComponents()
        self.show()

    def UiComponents(self):
        self.count = 0
        self.start = False

        button = QPushButton("Set Waktu (detik)", self)
        button.setGeometry(125, 100, 150, 50)
        button.clicked.connect(self.get_seconds)

        self.label = QLabel("//TIMER//", self)
        self.label.setGeometry(100, 200, 200, 50)
        self.label.setStyleSheet("border: 3px solid black")
        self.label.setFont(QFont('Times', 15))
        self.label.setAlignment(Qt.AlignCenter)

        start_button = QPushButton("Mulai", self)
        start_button.setGeometry(125, 350, 150, 40)
        start_button.clicked.connect(self.start_action)

        pause_button = QPushButton("Jeda", self)
        pause_button.setGeometry(125, 400, 150, 40)
        pause_button.clicked.connect(self.pause_action)

        reset_button = QPushButton("Reset", self)
        reset_button.setGeometry(125, 450, 150, 40)
        reset_button.clicked.connect(self.reset_action)

        timer = QTimer(self)
        timer.timeout.connect(self.showTime)
        timer.start(100)

    def showTime(self):
        if self.start:
            self.count -= 1
            if self.count == 0:
                self.start = False
                self.label.setText("Selesai !!!!")
            if self.start:
                text = str(self.count / 10) + " detik"
                self.label.setText(text)

    def get_seconds(self):
        self.start = False
        second, done = QInputDialog.getInt(self, 'Detik', 'Masukkan detik:')
        if done:
            self.count = second * 10
            self.label.setText(str(second))

    def start_action(self):
        self.start = True
        if self.count == 0:
            self.start = False

    def pause_action(self):
        self.start = False

    def reset_action(self):
        self.start = False
        self.count = 0
        self.label.setText("")

app = QApplication(sys.argv)
window = Window()
sys.exit(app.exec_())
