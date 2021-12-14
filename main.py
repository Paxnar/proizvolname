import sys

from random import choice
from Ui import Ui_MainWindow
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget


class MyWidget(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.do_paint = False
        self.pushButton.clicked.connect(self.run)
        # Обратите внимание: имя элемента такое же как в QTDesigner

    def paintEvent(self, event):
        if self.do_paint:
            qp = QPainter()
            qp.begin(self)
            self.draw_circle(qp)
            qp.end()

    def draw_circle(self, qp):
        qp.setBrush(QColor(choice(range(0, 256)), choice(range(0, 256)), choice(range(0, 256))))
        size = choice(range(25, 300))
        qp.drawEllipse(self.width() // 2 - size // 2, self.height() // 2 - size // 2, size, size)
        # Имя элемента совпадает с objectName в QTDesigner

    def run(self):
        self.do_paint = True
        self.repaint()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())