"""
Minimal PySide6/PySide2 launcher for AI Dev IDE.

This file provides a `launch(provider, url, model, token)` function
expected by `launcher.py`. If a full Qt frontend is not implemented,
we create a simple QMainWindow placeholder so the application can run
in environments where PySide is available (e.g., the Docker image).
"""
from typing import Optional
import sys

try:
    from PySide6.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout, QWidget
    from PySide6.QtCore import Qt
    PYSIDE = "PySide6"
except Exception:
    try:
        from PySide2.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout, QWidget
        from PySide2.QtCore import Qt
        PYSIDE = "PySide2"
    except Exception:
        QApplication = None  # type: ignore
        PYSIDE = None


def _create_placeholder_window(provider: str, model: str) -> QMainWindow:
    win = QMainWindow()
    win.setWindowTitle(f"AI Dev IDE ({PYSIDE})")
    win.setGeometry(100, 100, 1200, 800)

    label = QLabel(f"AI Dev IDE running with provider={provider}, model={model}")
    label.setAlignment(Qt.AlignCenter)

    central = QWidget()
    layout = QVBoxLayout()
    layout.addWidget(label)
    central.setLayout(layout)
    win.setCentralWidget(central)
    return win


def launch(provider: str = "openai", url: str = "", model: str = "gpt-4o", token: str = ""):
    """Create and return a Qt application instance. Caller should call `app.exec()`.

    Returns the `QApplication` instance if PySide is available, otherwise raises ImportError.
    """
    if QApplication is None:
        raise ImportError("Neither PySide6 nor PySide2 is available")

    app = QApplication(sys.argv)
    window = _create_placeholder_window(provider, model)
    window.show()
    return app
