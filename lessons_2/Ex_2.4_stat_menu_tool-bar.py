import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QAction, qApp, QDesktopWidget, QMessageBox
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
        exitAction = QAction(QIcon('exit-svgrepo-com.svg'), '&Exit', self)   # создаем действие с соответствующей иконкой
        exitAction_2 = QAction(QIcon('exit-svgrepo-com_2.svg'), '&Exit', self)
        exitAction.setShortcut('Ctrl+Q')  # для этого действия определяется комбинация клавиш
        exitAction_2.setShortcut('Ctrl+Q')  # для этого действия определ�
        exitAction.setStatusTip('Exit application')  # создает подсказку, которая показывается в строке состояния, когда вы наведёте указатель мыши на пункт меню
        exitAction_2.setStatusTip('Exit application')
        # Когда мы выбираем именно это действие, срабатывает сигнал.
        # Сигнал подключен к методу quit() виджета QApplication. Это завершает приложение.
        exitAction.triggered.connect(qApp.quit)
        exitAction_2.triggered.connect(qApp.quit)

        menubar = self.menuBar()
        fileMenu = menubar.addMenu('&File')
        fileMenu.addAction(exitAction)

        self.toolbar = self.addToolBar('Exit')
        self.toolbar.addAction(exitAction)


        self.setGeometry(300, 300, 250, 150)
        self.center()
        self.setWindowTitle('Statusbar')
        self.show()

    def center(self):  # для размещения активного окна по центру монитора
        qr = self.frameGeometry()  # Мы получаем прямоугольник, определяющий геометрию главного окна.
        cp = QDesktopWidget().availableGeometry().center()  # Мы получаем разрешение экрана нашего монитора. И с этим разрешением, мы получаем центральную точку.
        qr.moveCenter(cp)  # мы установили центр прямоугольника в центре экрана
        # Мы двигаем верхний левый угол окна приложения в верхний левый угол прямоугольника qr, таким образом, центрируя окно на нашем экране.
        self.move(qr.topLeft())

    def closeEvent(self, event):  # функция дя всплывающего окна при закрытии приложения
        # Третий аргумент определяет комбинацию кнопок, появляющихся в диалоге.
        # Последний параметр - кнопка по умолчанию. Это кнопка, на которой изначально установлен фокус клавиатуры.
        reply = QMessageBox.question(self, 'Message', 'Are you sure you want to quit?',
                                     QMessageBox.Yes | QMessageBox.No, QMessageBox.No)

        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())