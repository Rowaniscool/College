# mainWindow.py

from PyQt5 import QtWidgets
from GUIS.pythonControlMain import MainFrame
from Functions.Calc import Calculator
from Functions.Notepad import Notepad
from Functions.Calender import Calender
from Functions.Web import Web
from Functions.Password import Password


class MainWindow:

    def __init__(self):

        self.window = QtWidgets.QMainWindow()

        # Create the GUI
        self.ui = MainFrame()
        self.ui.setupUi(self.window)

        self.notepad = Notepad(self.ui)
        self.calculator = Calculator(self.ui)
        self.calender = Calender(self.ui)        
        self.web = Web(self.ui)
        self.password = Password(self.ui)


        self.ui.CalcButton.clicked.connect(lambda: self.changePage(0))
        self.ui.NotepadButon.clicked.connect(lambda: self.changePage(1))
        self.ui.CalenderButton.clicked.connect(lambda: self.changePage(2))
        self.ui.WebButton.clicked.connect(lambda: self.changePage(3))
        self.ui.PasswordButton.clicked.connect(lambda: self.changePage(4))



    def show(self): # Actually display the window 
        self.window.show()

    def changePage(self, indexPage=0):
        self.ui.stackedWidget.setCurrentIndex(indexPage)