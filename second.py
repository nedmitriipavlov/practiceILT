from PyQt6.QtWidgets import QApplication, QLabel, QMainWindow, QWidget
from PyQt6.QtGui import QImage, QColor, QPainter
from PyQt6.QtCore import QRectF, QEvent, Qt
import sys

class MainWindow(QMainWindow):
    def __init__(self):
       super(MainWindow, self).__init__()
       self.image = QImage()
       self.init_image(self.size())
       self.resize(320, 340)
       self.setWindowTitle('MyApp')
       self.installEventFilter(self)
       self.isInResize = False
       self.flag = False


    def init_image(self, size):
        self.image = QImage(size.width(), size.height(), QImage.Format.Format_ARGB32)


    def paintEvent(self, e):
        if self.isInResize:
            return
        width = self.width()
        height = self.height()
        for x in range(width):
            for y in range(height):
                self.image.setPixel(x, y, QColor(int(255 * x / width),
                                                 int(255 * y / height), 255).rgb())
        painter = QPainter(self)
        painter.drawImage(QRectF(0, 0, width, height), self.image)


    def resizeEvent(self, event):
        if not self.flag:
            self.isInResize = False
            self.flag = True
            self.endResize()
            return
        self.isInResize = True



    def endResize(self):
        self.isInResize = False
        self.image = QImage(self.size(), QImage.Format.Format_ARGB32)
        self.update()



    def eventFilter(self, obj, event):
        if self.isInResize:
            if event.type() == QEvent.Type.MouseButtonRelease:
                if (event.button() == Qt.MouseButton.LeftButton):
                    self.endResize()

            elif event.type() == QEvent.Type.NonClientAreaMouseButtonRelease:
                self.endResize()

        return super().eventFilter(obj, event)

app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()

