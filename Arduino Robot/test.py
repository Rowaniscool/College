import requests
import time
import socket
from PyQt5 import QtCore

HOST = "192.168.4.1"
PORT = 100
ESP32_IP = "http://192.168.40.124"

Robot = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
Robot.connect((HOST, PORT))
Robot.settimeout(0.05)

def Send(data):
    try:
        Robot.sendall(data)
    except Exception as e:
        print("Socket Error:", e)


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

heartbeatTimer = QtCore.QTimer()
heartbeatTimer.timeout.connect(HandleHeartbeat)
heartbeatTimer.start(50)



while True:
    try:
        response = requests.get(ESP32_IP + "/Button", timeout=1)
        Direction = response.text.strip()

        print(Direction)

        if Direction == "Right":
            Send(b'{"N":102,"D1":4,"D2":255}')

        elif Direction == "Left":
            Send(b'{"N":102,"D1":3,"D2":255}')

        elif Direction == "Forward":
            Send(b'{"N":102,"D1":1,"D2":255}')

        elif Direction == "Backward":
            Send(b'{"N":102,"D1":2,"D2":255}')

        elif Direction == "Stop":
            Send(b'{"N":102,"D1":9,"D2":0}')

    except requests.exceptions.RequestException:
        print("Couldn't connect to ESP32")

    time.sleep(0.1)