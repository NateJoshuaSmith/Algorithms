from PySide6.QtWidgets import QApplication
from widget import Widget
import sys
import time

app = QApplication(sys.argv)

window = Widget()
window.show()

app.exec()