import sys
from PyQt5 import QtWidgets
from ControlRemotely import MainRobot 

#Website is: http://192.168.4.1

app = QtWidgets.QApplication(sys.argv)

window = MainRobot()
window.show() #Showing login dashboard

sys.exit(app.exec_())