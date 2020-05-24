from PySide2.QtWidgets import *


class Window2(QWidget):
    def __init__(self):
        QWidget.__init__(self)

        self.layout = QHBoxLayout()

        self.progressBar = QProgressBar()
        self.slider = QSlider()
        self.slider.valueChanged.connect(self.evolutionBarre)


        self.layout.addWidget(self.progressBar)
        self.layout.addWidget(self.slider)


        self.setLayout(self.layout)


    def evolutionBarre(self):
        value = self.slider.value()
        self.progressBar.setValue(value)



if __name__ == "__main__" :
    app = QApplication([])
    win = Window2()
    win.show()
    app.exec_()
