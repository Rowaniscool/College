from GUIS.pythonControlMain import MainFrame
from PyQt5 import QtWidgets
import tkinter

from tkinter import filedialog, messagebox
class Notepad:
    def __init__(self, ui):
        self.ui = ui
        self.ui.pushButton.clicked.connect(self.saveFile)
        self.ui.pushButton_2.clicked.connect(self.openFile)
        self.ui.pushButton_3.clicked.connect(self.clearBox)

    def saveFile(self):
        text = self.ui.plainTextEdit.toPlainText()
        filePath = filedialog.asksaveasfilename(title="Save as file",initialdir=".", defaultextension=".txt")

        if filePath:
            try:
                with open(filePath, '+a') as file:
                    file.write(str(text))
                messagebox.showinfo("Successfully Saved")

            except Exception as e:
                messagebox.showerror(f"Error: {e}")


    def openFile(self):
        filePath = filedialog.askopenfilename(title="Open File", initialdir=".")

        if filePath:
            try:
                with open(filePath, 'r') as text:
                    content = text.read()
                self.ui.plainTextEdit.setPlainText(content)

            except Exception as e:
                messagebox.showerror(f"Error: {e}")


    def clearBox(self):
        self.ui.plainTextEdit.setPlainText("")      