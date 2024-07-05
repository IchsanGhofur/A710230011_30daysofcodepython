import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QLineEdit, QVBoxLayout, QWidget

class KasirApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Aplikasi Kasir")
        self.setGeometry(100, 100, 400, 200)

        # Label dan input harga
        self.label_harga = QLabel("Harga barang:")
        self.input_harga = QLineEdit()

        # Tombol hitung total
        self.btn_hitung = QPushButton("Hitung Total")
        self.btn_hitung.clicked.connect(self.hitung_total)

        # Label hasil total
        self.label_total = QLabel("Total: ")

        # Layout
        layout = QVBoxLayout()
        layout.addWidget(self.label_harga)
        layout.addWidget(self.input_harga)
        layout.addWidget(self.btn_hitung)
        layout.addWidget(self.label_total)

        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

    def hitung_total(self):
        try:
            harga = float(self.input_harga.text())
            pajak = 0.1  # Contoh: pajak 10%
            total = harga + (harga * pajak)
            self.label_total.setText(f"Total: ${total:.2f}")
        except ValueError:
            self.label_total.setText("Masukkan harga yang valid")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = KasirApp()
    window.show()
    sys.exit(app.exec_())
