import sys
from PyQt5.QtWidgets import QApplication, QWidget, QToolTip, QPushButton, QMessageBox
from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtCore import QCoreApplication


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

        qbtn = QPushButton('Quit', self)  # Вторым параметром является родительский виджет Example

        # Если мы нажмем на кнопку, вызовется сигнал "нажатие". Слот может быть слот Qt или любая Python функция
        # QCoreApplication содержит главный цикл обработки; он обрабатывает и диспетчеризирует все события.
        # Метод instance() дает нам его текущий экземпляр
        qbtn.clicked.connect(QCoreApplication.instance().quit)
        qbtn.resize(qbtn.sizeHint())
        qbtn.move(150, 50)

        self.setGeometry(300, 300, 300, 220)  # сочетает в себе методы resize() и move()
        # Первые два параметра х и у - это позиция окна. Третий - ширина, и четвертый - высота окна
        self.setWindowTitle('Icon')
        self.setWindowIcon(QIcon('qt-svgrepo-com.svg'))  # метод устанавливает иконку приложения

        self.show()

    def closeEvent(self, event):
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