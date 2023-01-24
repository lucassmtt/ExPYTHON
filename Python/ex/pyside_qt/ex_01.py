from PySide6.QtWidgets import (
    QApplication, QLabel, QPushButton, QWidget, QVBoxLayout, QMainWindow,
)
from PySide6.QtCore import Qt
from PySide6.QtGui import QFont, QAction

class Window(QMainWindow):
    def __init__(self):
        super().__init__()

        base = QWidget()
        layout = QVBoxLayout()

        font_do_label = QFont()
        font_do_label.setPixelSize(50)
        base.setFont(font_do_label)

        label = QLabel('Olá mundo')
        label.setAlignment(Qt.AlignCenter)

        botao = QPushButton('Click')

        layout.addWidget(label)
        layout.addWidget(botao)

        base.setLayout(layout)
        self.setCentralWidget(base)
        self.setWindowTitle('Meus testes')

        action = QAction('Ação', self)
        menu = self.menuBar()
        menu_geral = menu.addMenu('Menu')
        menu_geral.addAction(action)

app = QApplication()

janela = Window()
janela.show()

app.exec()