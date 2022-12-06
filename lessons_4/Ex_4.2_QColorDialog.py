# QColorDialog - виджет диалога для выбора цветовых значений.
import sys
from PyQt5.QtWidgets import QWidget, QPushButton, QFrame, QColorDialog, QApplication
from PyQt5.QtGui import QColor

class Example(QWidget):
    def __init__(self):
        super().__init__()  # возвращает родительский объект Example c классом
        self.initUI()

    def initUI(self):
        col = QColor(0, 0, 0)  # первоначальный цвет фона QtGui.QFrame
        self.btn = QPushButton('Dialog', self)
        self.btn.move(20, 20)

        self.btn.clicked.connect(self.showDialog)

        self.frm = QFrame(self)  # окно для цвета
        self.frm.setStyleSheet('Qwidget { background-color: %s }' % col.name())  # применяем для окна цвет по умолчанию
        self.frm.setGeometry(130, 22, 100, 100)  # применяем размер окна дя цвета

        self.setGeometry(300, 300, 250, 180)
        self.setWindowTitle('Color Dialog')
        self.show()

    def showDialog(self):
        col = QColorDialog.getColor()  # высветит QColorDialog.

        # проверяем, является ли цвет валидным. Если мы нажимаем кнопку «Cancel», возвращается невалидный цвет.
        # Если цвет валиден, мы меняем цвет фона, используя таблицы стилей (CSS)
        if col.isValid():
            self.frm.setStyleSheet('QWidget { background-color: %s }' % col.name())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())