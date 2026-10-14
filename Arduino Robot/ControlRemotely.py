from PyQt5 import QtCore, QtGui, QtWidgets
import socket
import cv2
import keyboard
import requests
from CameraRoute import RemoteCamera
from ControlRemotelyGui import MainGUI


class MainRobot(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        self.ui = MainGUI()
        self.ui.setupUi(self)

        # ---------------- Camera Connection ---------------- 

        self.RemoteCamera = RemoteCamera("http://192.168.4.1:81/stream")

        self.cameraTimer = QtCore.QTimer()
        self.cameraTimer.timeout.connect(self.UpdateCamera)
        self.cameraTimer.start(30)

        # ---------------- Robot ---------------- 

        HOST = "192.168.4.1"
        PORT = 100



        # Heartbeat timer
        self.heartbeatTimer = QtCore.QTimer()
        self.heartbeatTimer.timeout.connect(self.HandleHeartbeat)
        self.heartbeatTimer.start(50)
        # ---------------- ESP32 Button Control ----------------




        # ---------------- Robot ----------------

        self.ESPIP = "http://192.168.40.124"

        self.Robot = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.Robot.connect((HOST, PORT))

        self.Robot.settimeout(0.05)

        # ESP32 buttons
        self.buttonTimer = QtCore.QTimer()
        self.buttonTimer.timeout.connect(self.CheckESP32)
        self.buttonTimer.start(100)


        # ---------------- Keyboard ---------------- 

        keyboard.add_hotkey('w', self.MoveForward)
        keyboard.add_hotkey('s', self.MoveBackwards)
        keyboard.add_hotkey('a', self.MoveLeft)
        keyboard.add_hotkey('d', self.MoveRight)

        keyboard.add_hotkey('q', self.MoveCameraLeft)
        keyboard.add_hotkey('e', self.MoveCameraRight)

        keyboard.on_release(self.StopCar)




    # -- Camera Output and stuff --
    def UpdateCamera(self):
        frame = self.RemoteCamera.get_frame()
        if frame is None:
            return

        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        h, w, ch = frame.shape
        image = QtGui.QImage(frame.data, w, h, ch * w, QtGui.QImage.Format_RGB888)

        pixmap = QtGui.QPixmap.fromImage(image)
        self.ui.CameraOutput.setPixmap(pixmap)

    def CheckESP32(self):
        try:
            response = requests.get(
                self.ESPIP + "/Button",
                timeout=0.2
            )

            Direction = response.text.strip()

            if Direction == "Forward":
                self.MoveForward()

            elif Direction == "Backward":
                self.MoveBackwards()

            elif Direction == "Left":
                self.MoveLeft()

            elif Direction == "Right":
                self.MoveRight()

            elif Direction == "Stop":
                self.Send(b'{"N":102,"D1":9,"D2":0}')

        except requests.exceptions.RequestException:
            pass


    def Send(self, data):
        try:
            self.Robot.sendall(data)
        except Exception as e:
            print("Socket Error:", e)

    # -- Heartbeat -- 
    def HandleHeartbeat(self):
        try:
            data = self.Robot.recv(1024)
            if data:
                print(data)

                if b"{Heartbeat}" in data:
                    self.Robot.sendall(b"{Heartbeat}")

        except socket.timeout:
            pass
        except BlockingIOError:
            pass
        except Exception as e:
            print("Heartbeat Error:", e)


    # -- Movement --
    def MoveForward(self):
        self.Send(b'{"N":102,"D1":1,"D2":255}')

    def MoveBackwards(self):
        self.Send(b'{"N":102,"D1":2,"D2":255}')

    def MoveLeft(self):
        self.Send(b'{"N":102,"D1":3,"D2":255}')

    def MoveRight(self):
        self.Send(b'{"N":102,"D1":4,"D2":255}')

    # -- Camera Movement -- 
    def MoveCameraLeft(self):
        self.Send(b'{"N":106,"D1":3}')
        self.Send(b'{ok}')

    def MoveCameraRight(self):
        self.Send(b'{"N":106,"D1":4}')
        self.Send(b'{ok}')

    # -- Stop Car -- 
    def StopCar(self, event):
        if event.name in ('w', 'a', 's', 'd', 'q', 'e'):
            self.Send(b'{"N":102,"D1":9,"D2":0}')


    # -- Close Connection
    def closeEvent(self, event):
        try:
            self.Send(b'{"N":102,"D1":9,"D2":0}')
            self.Robot.close()
        except:
            pass

        event.accept()


#Robot.sendall(b'{"N":102, "D1":1, "D2":255}') Forward
#Robot.sendall(b'{"N":102, "D1":3, "D2":255}') Left
#Robot.sendall(b'{"N":102, "D1":4, "D2":255}') Right
#Robot.sendall(b'{"N":102, "D1":2, "D2":255}') Backwards
#Robot.sendall(b'{"N":102, "D1":9, "D2":0}') Stop
#Robot.sendall(b'{"N":106, "D1":3}') Camera Left
#Robot.sendall(b'{"N":106, "D1":4}') Camera Right
#Robot.sendall(b'{ok}') Camera Execute