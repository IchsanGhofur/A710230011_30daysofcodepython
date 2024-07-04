import sys
import time
from PyQt5.QtCore import QTime, QTimer
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QTimeEdit, QPushButton, QMessageBox

class AlarmClock(QWidget):
    def __init__(self):
        super().__init__()
        
        self.initUI()
    
    def initUI(self):
        self.setWindowTitle('Waker')
        
        layout = QVBoxLayout()

        self.timeLabel = QLabel('atur waktu:')
        layout.addWidget(self.timeLabel)
        
        self.timeEdit = QTimeEdit()
        self.timeEdit.setDisplayFormat('HH:mm:ss')
        layout.addWidget(self.timeEdit)
        
        self.setButton = QPushButton('atur alarm')
        self.setButton.clicked.connect(self.setAlarm)
        layout.addWidget(self.setButton)
        
        self.statusLabel = QLabel('')
        layout.addWidget(self.statusLabel)
        
        self.setLayout(layout)
        
        self.timer = QTimer()
        self.timer.timeout.connect(self.checkAlarm)
    
    def setAlarm(self):
        self.alarmTime = self.timeEdit.time()
        self.statusLabel.setText(f'alarm diatur untuk {self.alarmTime.toString()}')
        self.timer.start(1000)
    
    def checkAlarm(self):
        currentTime = QTime.currentTime()
        if currentTime == self.alarmTime:
            self.timer.stop()
            self.showAlarmMessage()
    
    def showAlarmMessage(self):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setText("Waktunya!")
        msg.setInformativeText(f'Alarm diatur untuk {self.alarmTime.toString()} bunyi.')
        msg.setWindowTitle('Alarm')
        msg.exec_()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    clock = AlarmClock()
    clock.show()
    sys.exit(app.exec_())
