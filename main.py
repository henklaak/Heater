import sys

from PySide6.QtWidgets import QApplication

from backend import Backend
from gui import MainWindow

SIMULATE = True

if __name__ == '__main__':
    app = QApplication(sys.argv)

    backend = Backend()
    main_window = MainWindow()
    main_window.set_backend(backend)
    main_window.show()

    sys.exit(app.exec())
