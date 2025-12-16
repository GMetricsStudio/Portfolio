from PySide6.QtCore import Signal
from PySide6.QtWidgets import QPushButton, QLabel
from UI.Pages.svg_page import SvgPage


class HomePage(SvgPage):
    logoutRequested = Signal()

    def __init__(self, svg_path):
        super().__init__(svg_path)
        
        # Welcome label
        self.welcome_label = QLabel("Welcome!", self.overlay)
        self.welcome_label.setGeometry(24, 120, 327, 40)
        self.welcome_label.setStyleSheet("""
            QLabel {
                color: black;
                font-size: 28px;
                font-weight: bold;
            }
        """)
        
        # User info label
        self.info_label = QLabel("Login to see your profile", self.overlay)
        self.info_label.setGeometry(24, 180, 327, 200)
        self.info_label.setStyleSheet("""
            QLabel {
                color: #333333;
                font-size: 16px;
                background: #F7F8F8;
                border-radius: 16px;
                padding: 20px;
            }
        """)
        self.info_label.setWordWrap(True)
        
        # Logout button
        logout_btn = QPushButton("Logout", self.overlay)
        logout_btn.setGeometry(24, 450, 327, 48)
        logout_btn.setStyleSheet("""
            QPushButton {
                background: #FF6B6B;
                color: white;
                border-radius: 24px;
                font-size: 16px;
                font-weight: bold;
            }
            QPushButton:pressed {
                background: #FF5252;
            }
        """)
        logout_btn.clicked.connect(self.logoutRequested.emit)

    def set_user_data(self, user_data: dict):
        name = f"{user_data.get('first', '')} {user_data.get('last', '')}".strip()
        if name:
            self.welcome_label.setText(f"Welcome, {name}!")
        
        info_text = f"""
        <div style='font-size: 16px; line-height: 1.6;'>
        <b>Email:</b> {user_data.get('email', '')}<br><br>
        <b>Gender:</b> {user_data.get('gender', '')}<br>
        <b>Date of Birth:</b> {user_data.get('dob', '')}<br>
        <b>Weight:</b> {user_data.get('weight', '')} kg<br>
        <b>Height:</b> {user_data.get('height', '')} cm
        </div>
        """
        self.info_label.setText(info_text)