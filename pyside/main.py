from PySide6.QtCore import Qt
from PySide6.QtGui import QFont, QAction
from PySide6.QtWidgets import (
    QApplication, QLabel, QPushButton, QWidget,
    QVBoxLayout, QMainWindow
)

from qdarktheme import load_stylesheet


def callback():
    print('Cliquei no botão!!!!')

def callback2():
    print('Callback 2!')



class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        base = QWidget()
        layout = QVBoxLayout()

        font = QFont()
        font.setPixelSize(90)
        base.setFont(font)

        self.label = QLabel('Deixa um Like!')
        self.label.setAlignment(Qt.AlignCenter)

        botao = QPushButton('Botão!')
        botao_new_window = QPushButton('Criar nova janela')

        botao.clicked.connect(self.muda_label)
        botao_new_window.clicked.connect(self.cria_janela)


        layout.addWidget(self.label)
        layout.addWidget(botao)
        layout.addWidget(botao_new_window)

        base.setLayout(layout)

        self.setCentralWidget(base)

        menu = self.menuBar()
        arquivo_menu = menu.addMenu('Arquivo')
        action = QAction('Print!')
        action.triggered.connect(callback2)
        arquivo_menu.addAction(action)

    def muda_label(self):
        if self.label.text() == 'Deixe um like!':
            self.label.setText('Clicado!!!!')
        else:
            self.label.setText('Deixe um like!')

    def cria_janela(self):
        nova_janela = Window()
        nova_janela.show()

app = QApplication()
app.setStyleSheet(load_stylesheet('light'))
janela = Window()
janela.show()

app.exec()