from PyQt5 import QtWidgets
from tkinter import filedialog

class Calender:
    def __init__(self, ui):
        self.ui = ui
        self.ui.scheduleEvents.clicked.connect(self.scheduleEvent)
        self.ui.viewEvents.clicked.connect(self.viewEventsFunc)
        self.ui.deleteEvent.clicked.connect(self.deleteEvents)


    def scheduleEvent(self):
        date = self.ui.dateEdit.date()
        event = self.ui.lineEdit.text()
        finalDate = str(date).translate(str.maketrans("", "", "()PyQt5.QtCore.QDate")) # Get rid of all chars except date

        fullStr = f"Name: {event} | Date: {finalDate}: \n"

   
        with open("Dates.txt", "a") as saveToFile:
            saveToFile.write(fullStr)

        self.ui.listWidget.addItem(fullStr)

    def viewEventsFunc(self):
        self.ui.listWidget.clear()

        with open("Dates.txt", "r") as viewFile:
            content = viewFile.readlines()

        for stuff in content:
            self.ui.listWidget.addItem(stuff)

    def deleteEvents(self):
        selectedItem = self.ui.listWidget.currentItem()

        if selectedItem:
            selectedText = selectedItem.text()

            with open("Dates.txt", "r") as file:
                content = file.read()

            content = content.replace(selectedText, "")

            with open("Dates.txt", "w") as file:
                file.write(content)

            self.viewEventsFunc()