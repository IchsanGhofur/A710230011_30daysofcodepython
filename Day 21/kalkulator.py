from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QGraphicsColorizeEffect
from PyQt5.QtCore import Qt
import sys

class CalculatorApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Kalkulator Sederhana")
        self.setGeometry(100, 100, 360, 350)
        self.createUI()
        self.show()

    def createUI(self):
        self.label = QLabel(self)
        self.label.setGeometry(5, 5, 350, 70)
        self.label.setWordWrap(True)
        self.label.setStyleSheet("QLabel { border: 4px solid black; background: white; }")
        self.label.setAlignment(Qt.AlignRight)
        

        # Buat tombol-tombol angka dan operator
        # Contoh: push1 = QPushButton("1", self)
        # Atur geometri dan hubungkan ke fungsi yang sesuai

        # Tombol sama dengan (=) dengan efek warna biru
        push_equal = QPushButton("=", self)
        push_equal.setGeometry(275, 300, 80, 40)
        color_effect = QGraphicsColorizeEffect()
        color_effect.setColor(Qt.blue)
        push_equal.setGraphicsEffect(color_effect)

        # Tombol-tombol operator lainnya (contoh: +, -, *, /)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = CalculatorApp()
    sys.exit(app.exec_())
