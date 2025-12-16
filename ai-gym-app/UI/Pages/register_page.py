import json
import os
import hashlib
from PySide6.QtCore import Signal, QDate
from PySide6.QtWidgets import (QPushButton, QLineEdit, QComboBox, 
                              QDateEdit, QMessageBox, QStackedWidget)
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
    with open(ACCOUNTS_FILE, "r") as f:
        return json.load(f)


def save_accounts(data):
    with open(ACCOUNTS_FILE, "w") as f:
        json.dump(data, f, indent=2)


class RegisterPage1(SvgPage):
    nextRequested = Signal()
    backRequested = Signal()

    def __init__(self, svg_path):
        super().__init__(svg_path)

        # Input fields
        self.first = QLineEdit(self.overlay)
        self.first.setPlaceholderText("First Name")
        self.first.setGeometry(32, 350, 310, 42)
        self.first.setStyleSheet("""
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

        self.last = QLineEdit(self.overlay)
        self.last.setPlaceholderText("Last Name")
        self.last.setGeometry(32, 410, 310, 42)
        self.last.setStyleSheet("""
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

        self.email = QLineEdit(self.overlay)
        self.email.setPlaceholderText("Email")
        self.email.setGeometry(32, 470, 310, 42)
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

        self.password = QLineEdit(self.overlay)
        self.password.setPlaceholderText("Password (min. 6 characters)")
        self.password.setEchoMode(QLineEdit.Password)
        self.password.setGeometry(32, 530, 260, 42)
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

        # Password toggle button
        toggle_pw = QPushButton("👁", self.overlay)
        toggle_pw.setGeometry(300, 530, 42, 42)
        toggle_pw.setStyleSheet("""
            QPushButton {
                background: #F5F5F5;
                border: 1px solid #E0E0E0;
                border-radius: 8px;
                font-size: 16px;
            }
        """)
        toggle_pw.clicked.connect(self.toggle_password)

        # Next button
        next_btn = QPushButton("Next", self.overlay)
        next_btn.setGeometry(24, 620, 327, 48)
        next_btn.setStyleSheet("""
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
        next_btn.clicked.connect(self.validate_and_next)

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

    def toggle_password(self):
        self.password.setEchoMode(
            QLineEdit.Normal
            if self.password.echoMode() == QLineEdit.Password
            else QLineEdit.Password
        )

    def validate_and_next(self):
        first = self.first.text().strip()
        last = self.last.text().strip()
        email = self.email.text().strip().lower()
        password = self.password.text()

        # Validation
        if not all([first, last, email, password]):
            QMessageBox.warning(self, "Error", "Please fill in all fields")
            return

        if len(password) < 6:
            QMessageBox.warning(self, "Error", "Password must be at least 6 characters")
            return

        if "@" not in email or "." not in email:
            QMessageBox.warning(self, "Error", "Please enter a valid email address")
            return

        # Check if email already exists
        accounts = load_accounts()
        if email in accounts:
            QMessageBox.warning(self, "Error", "Email already registered")
            return

        self.nextRequested.emit()


class RegisterPage2(SvgPage):
    backRequested = Signal()
    registerSuccess = Signal(dict)

    def __init__(self, svg_path):
        super().__init__(svg_path)

        # Gender selector
        self.gender = QComboBox(self.overlay)
        self.gender.addItems(["Select Gender", "Male", "Female", "Other", "Prefer not to say"])
        self.gender.setGeometry(32, 350, 310, 42)
        self.gender.setStyleSheet("""
            QComboBox {
                background: white;
                border: 1px solid #E0E0E0;
                border-radius: 8px;
                padding: 0 12px;
                font-size: 16px;
                color: black;
            }
            QComboBox::item {
                color: black;
            }
            QComboBox::item:selected {
                color: black;
            }
        """)

        # Date of Birth
        self.dob = QDateEdit(self.overlay)
        self.dob.setDate(QDate.currentDate().addYears(-20))
        self.dob.setCalendarPopup(True)
        self.dob.setGeometry(32, 410, 310, 42)
        self.dob.setStyleSheet("""
            QDateEdit {
                background: white;
                border: 1px solid #E0E0E0;
                border-radius: 8px;
                padding: 0 12px;
                font-size: 16px;
                color: black;
            }
        """)

        # Weight field
        self.weight = QLineEdit(self.overlay)
        self.weight.setPlaceholderText("Weight (kg)")
        self.weight.setGeometry(32, 470, 310, 42)
        self.weight.setStyleSheet("""
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

        # Height field
        self.height = QLineEdit(self.overlay)
        self.height.setPlaceholderText("Height (cm)")
        self.height.setGeometry(32, 530, 310, 42)
        self.height.setStyleSheet("""
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

        # Register button
        register_btn = QPushButton("Complete Registration", self.overlay)
        register_btn.setGeometry(24, 620, 327, 48)
        register_btn.setStyleSheet("""
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
        register_btn.clicked.connect(self.try_register)

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

    def try_register(self):
        # Get reference to RegisterPage1 through parent stack
        parent = self.parent()
        while parent and not isinstance(parent, QStackedWidget):
            parent = parent.parent()
        
        register1 = None
        if parent:
            for i in range(parent.count()):
                widget = parent.widget(i)
                if isinstance(widget, RegisterPage1):
                    register1 = widget
                    break
        
        if not register1:
            QMessageBox.warning(self, "Error", "Registration data not found")
            return

        # Validate RegisterPage2 fields
        if self.gender.currentIndex() == 0:
            QMessageBox.warning(self, "Error", "Please select your gender")
            return

        try:
            weight = float(self.weight.text().strip())
            if weight <= 0 or weight > 300:
                QMessageBox.warning(self, "Error", "Please enter a valid weight (1-300 kg)")
                return
        except ValueError:
            QMessageBox.warning(self, "Error", "Please enter a valid weight")
            return

        try:
            height = float(self.height.text().strip())
            if height <= 0 or height > 300:
                QMessageBox.warning(self, "Error", "Please enter a valid height (1-300 cm)")
                return
        except ValueError:
            QMessageBox.warning(self, "Error", "Please enter a valid height")
            return

        accounts = load_accounts()
        email = register1.email.text().strip().lower()

        if email in accounts:
            QMessageBox.warning(self, "Error", "Account already exists")
            return

        # Create user data
        payload = {
            "first": register1.first.text().strip(),
            "last": register1.last.text().strip(),
            "email": email,
            "password": hash_password(register1.password.text()),
            "gender": self.gender.currentText(),
            "dob": self.dob.date().toString("yyyy-MM-dd"),
            "weight": str(weight),
            "height": str(height)
        }

        # Save to local storage
        accounts[email] = payload
        save_accounts(accounts)

        QMessageBox.information(self, "Success", "Account created successfully!")
        
        # Clear sensitive data
        register1.password.clear()
        
        # Emit success signal
        self.registerSuccess.emit(payload)