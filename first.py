from PyQt6.QtWidgets import QApplication, QLabel, QMainWindow
import sys


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.label = QLabel('Push any button')

        self.setCentralWidget(self.label)

    def keyPressEvent(self, e):
        self.label.setText('keyPressed {0}'.format(str(e.key())))

    def keyReleaseEvent(self, e):
        keycode = e.key()
        if 0 <= keycode <= 255:
            self.label.setText('keyReleased {0}'.format(chr(keycode)))
        else:
            self.label.setText('keyReleased {0}'.format(e.text()))



app = QApplication(sys.argv)

window = MainWindow()
window.setFocus()
window.show()

app.exec()
