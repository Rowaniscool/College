from PyQt5 import QtWidgets
from GUIS.loginGUI import LoginGUI
from sqlstuff.init import makeEntry
from controlMain import MainWindow
import sqlite3
import sys

class LoginWindow:

    def __init__(self):
        self.window = QtWidgets.QMainWindow()

        self.ui = LoginGUI()
        self.ui.setupUi(self.window)

        self.ui.loginButton.clicked.connect(self.login)
        self.ui.registerButton.clicked.connect(self.register)
        self.app = QtWidgets.QApplication(sys.argv)


    def startGUI(self):
        self.mainWindow = MainWindow()
        self.mainWindow.show()
        self.window.close()


    def login(self):
        conn = sqlite3.connect("ElDataBase.db")
        cur = conn.cursor()
        info = cur.fetchall()

        username = self.ui.usernameInput.text()
        password = self.ui.passwordInput.text()

        cur.execute(
            "SELECT username, password FROM Users WHERE username = ?",
            (username,)
        )
        info = cur.fetchone()
        if info:
            storedUsername = info[0]
            storedPassword = info[1]

            if password == storedPassword:
                print("Login Successful")
                self.startGUI()
            else:
                print("Not successful")

                

    def register(self):
        username = self.ui.usernameInput.text()
        password = self.ui.passwordInput.text()
        username.strip(' ')
        password.strip(' ')
        makeEntry(username, password)

    def show(self):
        self.window.show()