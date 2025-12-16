from PySide6.QtSvgWidgets import QSvgWidget
from PySide6.QtWidgets import QWidget

class SvgPage(QWidget):
    def __init__(self, svg_path, w=375, h=812):
        super().__init__()
        self.setFixedSize(w, h)
        self.bg = QSvgWidget(svg_path, self)
        self.bg.setGeometry(0, 0, w, h)
        self.overlay = QWidget(self)
        self.overlay.setGeometry(0, 0, w, h)