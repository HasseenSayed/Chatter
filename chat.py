import socket

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect(("192.168.1.10", 5678))
    s.sendall("Hii :3")
    print(s.recv(1024))
