import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QAction, qApp
from PyQt5.QtGui import QIcon


class Example(QMainWindow):

    def __init__(self):
        super().__init__()  # возвращает родительский объект Example c классом
        self.initUI()

    def initUI(self):
        # Первый вызов метода создает строку состояния
        # Последующие вызовы возвращают объект статусбара. showMessage() отображает сообщение в строке состояния.
        self.statusBar().showMessage('Ready')


        #  QAction является абстракцией для действий, совершенных из меню, панели инструментов, или комбинаций клавиш
        exitAction = QAction(QIcon('exit-svgrepo-com.svg'), '&Exit', self)  # создаем действие с соответствующей иконкой
        exitAction.setShortcut('Ctrl+Q')  # для этого действия определяется комбинация клавиш
        exitAction.setStatusTip('Exit application')  # создает подсказку, которая показывается в строке состояния, когда вы наведёте указатель мыши на пункт меню

        # Когда мы выбираем именно это действие, срабатывает сигнал.
        # Сигнал подключен к методу quit() виджета QApplication. Это завершает приложение.
        exitAction.triggered.connect(qApp.quit)

        #self.statusBar()

        menubar = self.menuBar()
        fileMenu = menubar.addMenu('&File')
        fileMenu.addAction(exitAction)


        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('Statusbar')
        self.show()



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())