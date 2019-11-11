
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, \
    QVBoxLayout, QWidget

def button_pressed():
    print('button pressed!!!!')


app = QApplication([])
win = QMainWindow()

central_widget = QWidget()
button = QPushButton('Test', central_widget)
button2 = QPushButton('Second Test', central_widget)

layout = QVBoxLayout(central_widget)
layout.addWidget(button2)
layout.addWidget(button)

# button.setGeometry(0,50,120,40)

button.clicked.connect(button_pressed)
button2.clicked.connect(button_pressed)

win.setCentralWidget(central_widget)

win.show()
app.exit(app.exec_())


