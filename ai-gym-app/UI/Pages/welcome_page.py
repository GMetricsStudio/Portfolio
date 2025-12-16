from PySide6.QtCore import Signal
from PySide6.QtWidgets import QPushButton
from UI.Pages.svg_page import SvgPage

class WelcomePage(SvgPage):
    loginRequested = Signal()
    registerRequested = Signal()

    def __init__(self, svg_path):
        super().__init__(svg_path)

        # Login button
        login_btn = QPushButton('Login', self.overlay)
        login_btn.setGeometry(24, 650, 327, 48)
        login_btn.setStyleSheet("""
            QPushButton {
                background: #FFFFFF;
                color: #92A3FD;
                border: 2px solid #92A3FD;
                border-radius: 24px;
                font-size: 16px;
                font-weight: bold;
            }
            QPushButton:pressed {
                background: #F5F5F5;
            }
        """)
        login_btn.clicked.connect(self.loginRequested.emit)

        # Register button
        register_btn = QPushButton('Create Account', self.overlay)
        register_btn.setGeometry(24, 710, 327, 48)
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
        register_btn.clicked.connect(self.registerRequested.emit)