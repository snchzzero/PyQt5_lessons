import sys
from PyQt5.QtWidgets import QMainWindow, QApplication

class Example(QMainWindow):

    def __init__(self):
        super().__init__()  # возвращает родительский объект Example c классом
        self.initUI()

    def initUI(self):
        # Первый вызов метода создает строку состояния
        # Последующие вызовы возвращают объект статусбара. showMessage() отображает сообщение в строке состояния.
        self.statusBar().showMessage('Ready')

        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('Statusbar')
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())