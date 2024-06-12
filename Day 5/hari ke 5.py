from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QVBoxLayout, QWidget
from PyQt5.QtCore import QTimer, QTime, Qt
import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Timer Sederhana")
        self.setGeometry(500, 500, 500, 500)
        self.star_button = QPushButton("Mulai")
        self.start_button.clicked.connect(self.open_timer_window)
        
        # Menambahkan tombol ke layout
        layout = QVBoxLayout()
        layout.addWidget(self.start_button)
        
        # Menyiapkan central widget
        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)