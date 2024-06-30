import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout

class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        # Tambahkan elemen GUI di sini
        label = QLabel("Halo, dunia!", self)
        button = QPushButton("Klik Saya", self)
        button.clicked.connect(self.on_button_click)

        # Atur tata letak
        layout = QVBoxLayout()
        layout.addWidget(label)
        layout.addWidget(button)
        self.setLayout(layout)

    def on_button_click(self):
        print("Tombol diklik!")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())
