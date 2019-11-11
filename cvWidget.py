# ------------------------------------------------- -----
# -------------------- cvwidget.py --------------------
# -------------------------------------------------- ----
from  PyQt5.QtWidgets import *
# from PyQt5 import QtWidgets
from  matplotlib.backends.backend_qt5agg  import  FigureCanvas

from  matplotlib.figure  import  Figure


class  cvWidget (QWidget):

    def  __init__ ( self ,  parent  =  None ):

        QWidget . __init__ ( self ,  parent )

        self . canvas  =  FigureCanvas ( Figure ())

        vertical_layout  =  QVBoxLayout ()
        vertical_layout . addWidget ( self . canvas )

        self.canvas.axes  =  self . canvas . figure . add_subplot ( 111 )
        self.setLayout(vertical_layout )