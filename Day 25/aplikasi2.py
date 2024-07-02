import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLabel

class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    
    def initUI(self):
        self.setWindowTitle('Aplikasi update')
        self.setGeometry(800, 800, 800, 600)

        layout = QVBoxLayout()
        
        self.label = QLabel('Halo, selmata datang!', self)
        layout.addWidget(self.label)
        
        self.button = QPushButton('klik disini', self)
        self.button.clicked.connect(self.on_click)
        layout.addWidget(self.button)
        
        self.setLayout(layout)
    
    def on_click(self):
        self.label.setText('tombol berhasil diklik')

def main():
    app = QApplication(sys.argv)
    ex = MyApp()
    ex.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
