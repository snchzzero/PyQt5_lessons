#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QToolTip, QPushButton
from PyQt5.QtGui import QIcon, QFont


class Example(QWidget):  # наследуется от класса QWidget

    def __init__(self):
        super().__init__()  # возвращает родительский объект Example c классом

        self.initUI()


    def initUI(self):

        QToolTip.setFont(QFont('Arial', 10))  # метод устанавливает шрифт, используемый для отображения подсказки
        self.setToolTip('This is a <b>QWidget</b> widget')  # Чтобы создать всплывающую подсказку на всем поле виджета

        btn = QPushButton('Button', self)
        btn.setToolTip('This is a <b>QPushButton</b> widget')

        btn.resize(btn.sizeHint())  # sizeHint() дает рекомендуемый размер для кнопки
        btn.move(50, 50)

        self.setGeometry(300, 300, 300, 220)  # сочетает в себе методы resize() и move()
        # Первые два параметра х и у - это позиция окна. Третий - ширина, и четвертый - высота окна
        self.setWindowTitle('Icon')
        self.setWindowIcon(QIcon('qt-svgrepo-com.svg'))  # метод устанавливает иконку приложения

        self.show()


if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())