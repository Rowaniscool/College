import sys

from sqlstuff.init import initDB
from PyQt5 import QtWidgets
from loginFile import LoginWindow


# init the db
initDB()

# start the gui
app = QtWidgets.QApplication(sys.argv)

window = LoginWindow()
window.show()

sys.exit(app.exec_())