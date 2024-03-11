import socket
from time import sleep

PORT = 5678

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect(("192.168.1.34", PORT))
    while True:
        msg = input("\n")
        s.sendall(b"" + msg.encode())
        data = s.recv(1024)
        if not data:
            break
        print(data.decode())
