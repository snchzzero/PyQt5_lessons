import sys
from PyQt5.QtWidgets import QApplication, QWidget


if __name__ == '__main__':

    app = QApplication(sys.argv)  # sys.argv - список аргументов командной строки

    w = QWidget()  # Виджет без родителей называется окно
    w.resize(250, 150)
    w.move(500, 500)  # двигает виджет на экране на координату
    w.setWindowTitle('Simple')
    w.show()

    sys.exit(app.exec_())