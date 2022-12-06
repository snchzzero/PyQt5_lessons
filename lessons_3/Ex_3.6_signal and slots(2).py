import sys
from PyQt5.QtWidgets import QMainWindow, QPushButton, QApplication


class Example(QMainWindow):

    def __init__(self):
        super().__init__()  # возвращает родительский объект Example c классом

        self.initUI()


    def initUI(self):

        btn1 = QPushButton("Button 1", self)
        btn1.move(30, 50)

        btn2 = QPushButton("Button 2", self)
        btn2.move(150, 50)

        btn1.clicked.connect(self.buttonClicked)  # Обе кнопки подключаются к одному слоту
        btn2.clicked.connect(self.buttonClicked)  # Обе кнопки подключаются к одному слоту

        self.statusBar()

        self.setGeometry(300, 300, 290, 150)
        self.setWindowTitle('Event sender')
        self.show()


    def buttonClicked(self):

        sender = self.sender()  # мы определяем, какую из кнопок мы нажали с помощью метода sender()
        self.statusBar().showMessage(sender.text() + ' was pressed')  # Мы определяем источник сигнала с помощью метода sender()


if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())