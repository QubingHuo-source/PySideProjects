# import sys
# from PySide6.QtCore import *
# from PySide6.QtGui import *
# from PySide6.QtWidgets import QApplication, QWidget, QPushButton, QLabel

# class ExampleWnd(QWidget):
#     def __init__(self):
#         super().__init__()

#         self.setup()

#     def setup(self):
#         self.setGeometry(100, 100, 200, 150)
#         self.show()

#         btn_quit = QPushButton('Quit',self)
#         btn_quit.clicked.connect(QApplication.instance().quit() )
#         btn_quit.show()
       
#         btn_quit.resize(btn_quit.sizeHint() )
#         btn_quit.move(90, 100)
        

# if __name__ == '__main__':

#     app = QApplication(sys.argv)

#     wnd = ExampleWnd()

#     wnd.show()
#     sys.exit( app.exec() )
#     # app = QApplication(sys.argv)

#     # label = QLabel("Hello World!")

#     # # label = QLabel("<font color=red size=40>Hello World!</font>")

#     # label.show()

#     # app.exec_()


import sys
import random
from PySide6 import QtCore, QtWidgets, QtGui


class MyWidget(QtWidgets.QWidget ):
    def __init__(self):
        super().__init__()

        self.str = ['hello','hey man', 'nihao']
        self.button = QtWidgets.QPushButton("Click me!")
        self.text = QtWidgets.QLabel("Hello World",alignment = QtCore.Qt.AlignCenter ) 

        self.layout = QtWidgets.QVBoxLayout(self)
        self.layout.addWidget(self.text)
        self.layout.addWidget(self.button)

        self.button.clicked.connect(self.magic)


    @QtCore.Slot()
    def magic(self):
        self.text.setText(random.choice(self.str))


if __name__ == '__main__':
    app = QtWidgets.QApplication([])

    widget = MyWidget()
    widget.resize(800, 600)
    widget.show()

    sys.exit(app.exec() )




