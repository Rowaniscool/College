import requests
import time
import socket


# ----------------- TESTING BEFORE CONVERTING TO GUI

HOST = "192.168.4.1"
PORT = 100

ESP32_IP = "http://192.168.40.124"

Robot = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
Robot.settimeout(5)
Robot.connect((HOST, PORT))

LastDirection = ""

while True:

    try:
        response = requests.get(ESP32_IP + "/Button", timeout=1)
        Direction = response.text.strip()

        # Only send when the direction changes
        if Direction != LastDirection:

            if Direction == "Forward":
                Robot.sendall(b'{"N":102,"D1":7,"D2":255}')

            elif Direction == "Backward":
                Robot.sendall(b'{"N":102,"D1":2,"D2":255}')

            elif Direction == "Left":
                Robot.sendall(b'{"N":102,"D1":3,"D2":255}')

            elif Direction == "Right":
                Robot.sendall(b'{"N":102,"D1":4,"D2":255}')

            elif Direction == "Stop":
                Robot.sendall(b'{"N":102,"D1":9,"D2":0}')

            print("Direction:", Direction)

            LastDirection = Direction

    except requests.exceptions.RequestException:
        print("Couldn't connect to ESP32")

    except (ConnectionAbortedError, ConnectionResetError, BrokenPipeError) as e:
        print("Robot connection lost:", e)
        break

    time.sleep(0.05)