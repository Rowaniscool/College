import socket
import time

HOST = "192.168.4.1"
PORT = 100


#Camera output http://192.168.4.1/

Robot = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
Robot.settimeout(5)
Robot.connect((HOST, PORT))


#Robot.sendall(b'{"N":102, "D1":1, "D2":255}') Forward
#Robot.sendall(b'{"N":102, "D1":3, "D2":255}') Left
#Robot.sendall(b'{"N":102, "D1":4, "D2":255}') Right
#Robot.sendall(b'{"N":102, "D1":2, "D2":255}') Backwards
#Robot.sendall(b'{"N":102, "D1":9, "D2":0}') Stop
#Robot.sendall(b'{"N":106, "D1":3}') Camera Left
#Robot.sendall(b'{"N":106, "D1":4}') Camera Right
#Robot.sendall(b'{ok}') Camera Execute


Robot.sendall(b'{"N":106, "D1":3}')
time.sleep(2)

Robot.sendall(b'{ok}')
Robot.close()