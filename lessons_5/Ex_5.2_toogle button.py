import sys
from PyQt5.QtWidgets import QWidget, QPushButton, QFrame, QApplication
from PyQt5.QtGui import QColor

class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.col = QColor(0, 0, 0)  # изначально цвет квадрата черный

        redb = QPushButton('Red', self)  # создаём три кнопки переключателя
        redb.setCheckable(True)  # делаем её проверяемой
        redb.move(10, 10)
        # привязываем сигнал к нашему пользовательскому методу. используем сигнал clicked, который работает с логическим значением.
        redb.clicked[bool].connect(self.setColor)

        greenb = QPushButton('Green', self)
        greenb.setCheckable(True)
        greenb.move(10, 60)
        greenb.clicked[bool].connect(self.setColor)

        blueb = QPushButton('Blue', self)
        blueb.setCheckable(True)
        blueb.move(10, 110)
        blueb.clicked[bool].connect(self.setColor)

        self.square = QFrame(self)
        self.square.setGeometry(150, 20, 100, 100)
        self.square.setStyleSheet("QWidget { background-color: %s }" % self.col.name())

        self.setGeometry(300, 300, 280, 170)
        self.setWindowTitle('Toggle button')
        self.show()

    def setColor(self, pressed):
        source = self.sender()  # получаем кнопку, которая была переключена
        if pressed:
            val = 255
        else:
            val = 0

        if source.text() == 'Red':
            self.col.setRed(val)
        elif source.text() == 'Green':
            self.col.setGreen(val)
        elif source.text() == 'Blue':
            self.col.setBlue(val)

        self.square.setStyleSheet("QFrame{ background-color: %s }" % self.col.name())  # используем таблицы стилей, чтобы менять цвет фона

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())

