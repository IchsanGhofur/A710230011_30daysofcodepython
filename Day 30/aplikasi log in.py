import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QLineEdit, QGridLayout, QMessageBox

class MainWindow(QWidget):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setWindowTitle("Log in sederhana")
        self.resize(800, 200)

        layout = QGridLayout()

        # Display username label and input field
        label_name = QLabel('<font size="5">Username: ')
        self.lineEdit_username = QLineEdit()
        self.lineEdit_username.setPlaceholderText("Masukkan Username: ")
        layout.addWidget(label_name, 0, 0)
        layout.addWidget(self.lineEdit_username, 0, 1)

        # Display password label and input field
        label_password = QLabel('<font size="5">Password: ')
        self.lineEdit_password = QLineEdit()
        self.lineEdit_password.setPlaceholderText("Masukkan Password: ")
        layout.addWidget(label_password, 1, 0)
        layout.addWidget(self.lineEdit_password, 1, 1)

        # Validate username and password
        def password_checker(self):
            message = QMessageBox()
            if self.lineEdit_username.text() == "pesonainformatika" and self.lineEdit_password.text() == "secret":
                message.setText("Berhasil Login")
                message.exec_()
                app.quit()
            else:
                message.setText("Password Anda salah")
                message.exec_()

        # Set login button
        button_login = QPushButton('Login')
        button_login.clicked.connect(password_checker)
        layout.addWidget(button_login, 2, 0, 1, 2)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
