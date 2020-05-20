from PySide2.QtWidgets import *

class  Window3(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.setMinimumSize(500,300)
        self.layout = QVBoxLayout()

        #self.button = QPushButton("ferme moi")
        #self.button.clicked.connect(self.close)
        #self.layout.addWidget(self.button)

        self.button2 = QPushButton()
        self.button2.clicked.connect(self.nbClick)
        self.layout.addWidget(self.button2)
        self.nb = 0

        self.text = QTextEdit("Le nombre de clics va être affiché ici")

        self.layout.addWidget(self.text)


        self.setLayout(self.layout)

    def nbClick(self):
        self.nb +=1
        self.button2.setText("clic "+ str(self.nb))
        self.text.setText("clic "+ str(self.nb))



if __name__ == "__main__" :
    app = QApplication([])
    win = Window3()
    win.show()
    app.exec_()
