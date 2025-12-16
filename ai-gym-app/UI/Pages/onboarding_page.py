from PySide6.QtCore import Signal
from PySide6.QtWidgets import QPushButton
from UI.Pages.svg_page import SvgPage

class OnboardingPage(SvgPage):
    nextRequested = Signal()
    backRequested = Signal()
    skipRequested = Signal()

    def __init__(self, svg_path, step_index, step_count):
        super().__init__(svg_path)

        # Next button
        next_btn = QPushButton('Next', self.overlay)
        next_btn.setGeometry(24, 730, 327, 48)
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
        next_btn.clicked.connect(self.nextRequested.emit)

        # Skip button
        skip_btn = QPushButton('Skip', self.overlay)
        skip_btn.setGeometry(24, 24, 80, 32)
        skip_btn.setStyleSheet("""
            QPushButton {
                background: transparent;
                color: #7B6F72;
                font-size: 14px;
                border: none;
            }
        """)
        skip_btn.clicked.connect(self.skipRequested.emit)

        # Back button (only show if not first page)
        if step_index > 1:
            back_btn = QPushButton('Back', self.overlay)
            back_btn.setGeometry(120, 24, 80, 32)
            back_btn.setStyleSheet("""
                QPushButton {
                    background: transparent;
                    color: #7B6F72;
                    font-size: 14px;
                    border: none;
                }
            """)
            back_btn.clicked.connect(self.backRequested.emit)