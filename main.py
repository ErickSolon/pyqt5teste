import sys
import ui

from PyQt5 import QtWidgets

class MainWindow(QtWidgets.QMainWindow, ui.Ui_MainWindow):

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.botao.clicked.connect(self.botao_action)

    def botao_action(self):
        self.status.setText("Botão está funcionando!!!")
        self.exibir_texto.setText("teste")

def main():
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec_()


if __name__ == '__main__':
    main()
