import sys
from PyQt5.QtWidgets import QWidget, QSlider, QLabel, QApplication, QGridLayout
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap

class Example(QWidget):
    def __init__(self):
        super().__init__()  # возвращает родительский объект Example c классом
        self.initUI()

    def initUI(self):
        sld = QSlider(Qt.Horizontal, self)  #  создаём горизонтальный ползунок
        sld.setFocusPolicy(Qt.NoFocus)
        sld.setGeometry(30, 40, 100, 30)
        sld.valueChanged[int].connect(self.changeValue)


        self.label = QLabel(self)
        self.label.setPixmap(QPixmap('levels-mute.svg').scaled(50, 50))  # scaled возвращает измененный размер
        self.label.setGeometry(200, 40, 100, 50)


        self.setGeometry(300, 300, 280, 170)
        self.setWindowTitle('QSlider')
        self.show()

    def changeValue(self, value):
        if value == 0:
            self.label.setPixmap(QPixmap('levels-mute.svg').scaled(50, 50))
        elif 0 < value <= 30:
            self.label.setPixmap(QPixmap('levels-low.svg').scaled(50, 50))
        elif 30 < value <= 80:
            self.label.setPixmap(QPixmap('levels-medium.svg').scaled(50, 50))
        elif 80 < value <= 100:
            self.label.setPixmap(QPixmap('levels-large.svg').scaled(50, 50))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())