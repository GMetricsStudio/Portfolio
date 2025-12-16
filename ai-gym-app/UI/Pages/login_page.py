import json
import os
import hashlib
from PySide6.QtCore import Signal, Qt
from PySide6.QtWidgets import QPushButton, QLineEdit, QLabel, QMessageBox
from UI.Pages.svg_page import SvgPage


DATA_DIR = "data"
ACCOUNTS_FILE = os.path.join(DATA_DIR, "accounts.json")

def hash_password(pw: str) -> str:
    return hashlib.sha256(pw.encode()).hexdigest()

def load_accounts():
    if not os.path.exists(DATA_DIR):
        os.makedirs(DATA_DIR)
    if not os.path.exists(ACCOUNTS_FILE):
        return {}
    try:
        with open(ACCOUNTS_FILE, "r") as f:
            return json.load(f)
    except:
        return {}

class LoginPage(SvgPage):
    backRequested = Signal()
    loginSuccess = Signal(dict)
    goToRegister = Signal()

    def __init__(self, svg_path):
        super().__init__(svg_path)

        # Email field
        self.email = QLineEdit(self.overlay)
        self.email.setPlaceholderText("Email")
        self.email.setGeometry(32, 350, 310, 42)
        self.email.setStyleSheet("""
            QLineEdit {
                background: white;
                border: 1px solid #E0E0E0;
                border-radius: 8px;
                padding: 0 12px;
                font-size: 16px;
                color: black;
            }
            QLineEdit::placeholder {
                color: #7B6F72;
            }
        """)

        # Password field
        self.password = QLineEdit(self.overlay)
        self.password.setPlaceholderText("Password")
        self.password.setEchoMode(QLineEdit.Password)
        self.password.setGeometry(32, 410, 310, 42)
        self.password.setStyleSheet("""
            QLineEdit {
                background: white;
                border: 1px solid #E0E0E0;
                border-radius: 8px;
                padding: 0 12px;
                font-size: 16px;
                color: black;
            }
            QLineEdit::placeholder {
                color: #7B6F72;
            }
        """)

        # Login button
        login_btn = QPushButton("Login", self.overlay)
        login_btn.setGeometry(24, 480, 327, 48)
        login_btn.setStyleSheet("""
            QPushButton {
                background: #92A3FD;
                color: white;
                border-radius: 24px;
                font-size: 16px;
                font-weight: bold;
            }
            QPushButton:pressed {
                background: #7B8EF5;
            }
        """)
        login_btn.clicked.connect(self.try_login)

        # Register link
        register_label = QLabel("Don't have an account?", self.overlay)
        register_label.setGeometry(90, 550, 195, 30)
        register_label.setStyleSheet("color: #7B6F72; font-size: 14px;")
        register_label.setAlignment(Qt.AlignCenter)

        register_btn = QPushButton("Sign Up", self.overlay)
        register_btn.setGeometry(90, 580, 195, 30)
        register_btn.setStyleSheet("""
            QPushButton {
                background: transparent;
                color: #92A3FD;
                font-size: 14px;
                font-weight: bold;
                border: none;
            }
            QPushButton:pressed {
                color: #7B8EF5;
            }
        """)
        register_btn.clicked.connect(self.goToRegister.emit)

        # Back button
        back_btn = QPushButton("← Back", self.overlay)
        back_btn.setGeometry(24, 24, 80, 32)
        back_btn.setStyleSheet("""
            QPushButton {
                background: transparent;
                color: #7B6F72;
                font-size: 14px;
                border: none;
            }
        """)
        back_btn.clicked.connect(self.backRequested.emit)

    def try_login(self):
        email = self.email.text().strip().lower()
        password = self.password.text()

        if not email or not password:
            QMessageBox.warning(self, "Error", "Please fill in all fields")
            return

        accounts = load_accounts()

        if email not in accounts:
            QMessageBox.warning(self, "Error", "Account not found")
            return

        stored_data = accounts[email]
        hashed_input = hash_password(password)

        if stored_data.get("password") != hashed_input:
            QMessageBox.warning(self, "Error", "Invalid password")
            return

        # Login successful
        user_data = {
            "first": stored_data.get("first", ""),
            "last": stored_data.get("last", ""),
            "email": email,
            "gender": stored_data.get("gender", ""),
            "dob": stored_data.get("dob", ""),
            "weight": stored_data.get("weight", ""),
            "height": stored_data.get("height", "")
        }

        self.loginSuccess.emit(user_data)