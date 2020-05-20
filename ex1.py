from PySide2.QtWidgets import *
import random

class Window(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.setMinimumSize(500,300)
        self.liste = ["CSI","CIR","BIOST","CENT",'BIAST',"EST"]
        self.layout = QVBoxLayout()


        self.label = QLabel()
        self.button = QPushButton("Changer de Cycle")
        self.button.clicked.connect(self.listeHasard)


        self.layout.addWidget(self.label)
        self.layout.addWidget(self.button)

        self.setLayout(self.layout)


    def listeHasard(self):
        txt = random.choice(self.liste)
        self.label.setText(txt)


if __name__ == "__main__" :
    app = QApplication([])
    win = Window()
    win.show()
    app.exec_()
