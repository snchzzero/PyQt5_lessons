import sys
from PyQt5.QtWidgets import QWidget, QPushButton, QHBoxLayout, QVBoxLayout, QApplication

class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        okButton = QPushButton("OK")
        cancelButton = QPushButton("Cancel")

        hbox = QHBoxLayout()  # создаём макет горизонтального блока
        hbox.addStretch(1)  # добавляем показатель растяжения
        hbox.addWidget(okButton)  # добавляем кнопку
        hbox.addWidget(cancelButton)  # добавляем кнопку

        vbox = QVBoxLayout()  # создаём макет вертикального блока
        vbox.addStretch(1)  # добавляем показатель растяжения
        vbox.addLayout(hbox)  # поставим горизонтальный макет в вертикальный

        self.setLayout(vbox)  # устанавливаем главный макет окна

        self.setGeometry(300, 300, 300, 150)
        self.setWindowTitle('Buttons')
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())