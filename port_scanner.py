import sys
import socket
from PyQt5.QtWidgets import (
    QApplication, QWidget, QLabel, QLineEdit,
    QPushButton, QTextEdit, QVBoxLayout, QMessageBox
)
from PyQt5.QtCore import QThread, pyqtSignal

# ================= THREAD =================
class PortScannerThread(QThread):
    result = pyqtSignal(str)

    def __init__(self, ip, start_port, end_port):
        super().__init__()
        self.ip = ip
        self.start_port = start_port
        self.end_port = end_port

    def run(self):
     for port in range(self.start_port, self.end_port + 1):
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(0.2)
            if s.connect_ex((self.ip, port)) == 0:
                mesaj = f"Açık Port: {port}"

                # GUI'ye yaz
                self.result.emit(mesaj)

                # DOSYAYA yaz
                with open("sonuclar.txt", "a", encoding="utf-8") as f:
                    f.write(mesaj + "\n")

            s.close()
        except:
            pass




# ================= ANA UYGULAMA =================
class PortScannerApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Basit Port Tarayıcı")
        self.setGeometry(400, 200, 420, 360)

        layout = QVBoxLayout()

        layout.addWidget(QLabel("IP Adresi:"))
        self.ip_input = QLineEdit("127.0.0.1")
        layout.addWidget(self.ip_input)

        layout.addWidget(QLabel("Başlangıç Port:"))
        self.start_port = QLineEdit("20")
        layout.addWidget(self.start_port)

        layout.addWidget(QLabel("Bitiş Port:"))
        self.end_port = QLineEdit("1024")
        layout.addWidget(self.end_port)

        self.scan_button = QPushButton("Taramayı Başlat")
        self.scan_button.clicked.connect(self.start_scan)
        layout.addWidget(self.scan_button)

        self.result_box = QTextEdit()
        self.result_box.setReadOnly(True)
        layout.addWidget(self.result_box)

        self.setLayout(layout)

    def start_scan(self):
        try:
            ip = self.ip_input.text()
            start = int(self.start_port.text())
            end = int(self.end_port.text())

            self.result_box.clear()
            self.result_box.append(f"Taranan IP: {ip}\n")

            self.thread = PortScannerThread(ip, start, end)
            self.thread.result.connect(self.result_box.append)
            self.thread.start()
        except:
            QMessageBox.warning(self, "Hata", "Port bilgileri geçersiz!")


# ================= GİRİŞ EKRANI =================
class Login(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Giriş")
        self.setGeometry(450, 300, 300, 150)

        layout = QVBoxLayout()

        layout.addWidget(QLabel("Şifre:"))
        self.password_input = QLineEdit()
        self.password_input.setEchoMode(QLineEdit.Password)
        layout.addWidget(self.password_input)

        self.login_button = QPushButton("Giriş Yap")
        self.login_button.clicked.connect(self.check_password)
        layout.addWidget(self.login_button)

        self.setLayout(layout)

    def check_password(self):
        if self.password_input.text() == "1234":  
            self.main = PortScannerApp()
            self.main.show()
            self.close()
        else:
            QMessageBox.critical(self, "Hata", "Şifre yanlış!")


# ================= DARK THEME =================
dark_theme = """
QWidget {
    background-color: #121212;
    color: #e0e0e0;
    font-size: 12px;
}
QLineEdit, QTextEdit {
    background-color: #1e1e1e;
    border: 1px solid #444;
    color: #ffffff;
}
QPushButton {
    background-color: #2b2b2b;
    border: 1px solid #555;
    padding: 6px;
}
QPushButton:hover {
    background-color: #3a3a3a;
}
"""

# ================= MAIN =================
if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyleSheet(dark_theme)
    login = Login()
    login.show()
    sys.exit(app.exec_())
