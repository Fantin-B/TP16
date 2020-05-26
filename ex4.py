from PySide2.QtWidgets import *

class Calculatrice(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.layout = QVBoxLayout()

        self.text = QTextEdit("0")
        self.layout.addWidget(self.text)
        self.text.setMaximumHeight(25)

        self.ligneButton1 = LigneButton(["C","CE"],self.text)
        self.layout.addWidget(self.ligneButton1)

        self.ligneButton2 = LigneButton(["7","8","9","/"],self.text)
        self.layout.addWidget(self.ligneButton2)

        self.ligneButton3 = LigneButton(["4","5","6","*"],self.text)
        self.layout.addWidget(self.ligneButton3)

        self.ligneButton4 = LigneButton(["1","2","3","-"],self.text)
        self.layout.addWidget(self.ligneButton4)

        self.ligneButton5 = LigneButton(["0",",","=","+"],self.text)
        self.layout.addWidget(self.ligneButton5)

        self.setLayout(self.layout)




class LigneButton(QWidget):
    def __init__(self,liste,text):
        QWidget.__init__(self)
        self.layout = QHBoxLayout()
        self.__liste = liste
        self.__text = text

        for i in self.__liste:
            self.Button = QPushButton(i)
            self.Button.clicked.connect(self.__text.setText(i))
            self.layout.addWidget(self.Button)

        self.setLayout(self.layout)



if __name__ == "__main__" :
    app = QApplication([])
    win = Calculatrice()
    win.show()
    app.exec_()
