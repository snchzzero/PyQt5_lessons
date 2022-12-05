import sys
from PyQt5.QtWidgets import QWidget, QDesktopWidget, QApplication

class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.resize(250, 150)
        self.center()

        self.setWindowTitle('Center')
        self.show()

    def center(self):
        qr = self.frameGeometry()  # Мы получаем прямоугольник, определяющий геометрию главного окна.
        cp = QDesktopWidget().availableGeometry().center()  # Мы получаем разрешение экрана нашего монитора. И с этим разрешением, мы получаем центральную точку.
        qr.moveCenter(cp)  # мы установили центр прямоугольника в центре экрана
        # Мы двигаем верхний левый угол окна приложения в верхний левый угол прямоугольника qr, таким образом, центрируя окно на нашем экране.
        self.move(qr.topLeft())  

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())