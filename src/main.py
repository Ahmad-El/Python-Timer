from PyQt6.QtWidgets import QApplication
from PyQt6.QtCore import QTimer

from mainwindow import MainWindow
import sys

app = QApplication(sys.argv)

window = MainWindow()
window.setFixedSize(500, 1308)
window.show()
timer = QTimer()
timer.setInterval(100)
timer.timeout.connect(window.set_time)
timer.start()


app.exec()
