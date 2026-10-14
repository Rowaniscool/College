
#listView
class Password:
    def __init__(self, ui):
        self.ui = ui

        self.ui.pushButton_7.clicked.connect(self.savePass)

    def savePass(self):
        password = self.ui.passwordEntry.text()
        usage = self.ui.sourceOfPass.text()
        stored = f"Password: {password}\n Usage: {usage}\n\n"

        with open("passwords.txt", "a") as file:
            file.write(stored)

        self.ui.listView.addItem(stored)

    def viewPass(self):
        pass

    def deletePass(self):
        pass