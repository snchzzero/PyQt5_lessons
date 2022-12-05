# Панель инструментов (тулбар)
# Меню группируют все команды, которые мы можем использовать в приложении.
# Панели инструментов обеспечивают быстрый доступ к наиболее часто используемым командам

import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QAction, qApp
from PyQt5.QtGui import QIcon


class Example(QMainWindow):

    def __init__(self):
        super().__init__()  # возвращает родительский объект Example c классом
        self.initUI()

    def initUI(self):



        #  QAction является абстракцией для действий, совершенных из меню, панели инструментов, или комбинаций клавиш
        exitAction = QAction(QIcon('exit-svgrepo-com_2.svg'), '&Exit', self)  # создаем действие с соответствующей иконкой
        exitAction.setShortcut('Ctrl+Q')  # для этого действия определяется комбинация клавиш

        # Когда мы выбираем именно это действие, срабатывает сигнал.
        # Сигнал подключен к методу quit() виджета QApplication. Это завершает приложение.
        exitAction.triggered.connect(qApp.quit)

        self.toolbar = self.addToolBar('Exit')
        self.toolbar.addAction(exitAction)


        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('Toolbar')
        self.show()



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())