import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QPushButton, QLineEdit

class CalculatorApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Kalkulator Sederhana")
        self.setGeometry(100, 100, 300, 200)

        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)

        layout = QVBoxLayout()
        self.display = QLineEdit()
        layout.addWidget(self.display)

        buttons = [
            "7", "8", "9", "/",
            "4", "5", "6", "*",
            "1", "2", "3", "-",
            "0", ".", "=", "+"
        ]

        for btn_text in buttons:
            button = QPushButton(btn_text)
            button.clicked.connect(self.handle_button_click)
            layout.addWidget(button)

        central_widget.setLayout(layout)

    def handle_button_click(self):
        sender = self.sender()
        current_text = self.display.text()

        if sender.text() == "=":
            try:
                result = eval(current_text)
                self.display.setText(str(result))
            except Exception:
                self.display.setText("Error")
        else:
            self.display.setText(current_text + sender.text())

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = CalculatorApp()
    window.show()
    sys.exit(app.exec_())
