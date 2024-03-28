import socket
import threading
import chatnet

PORT = 5678

def receiver(s):
    while True:
        data = s.recv(1024)
        if not data:
            break
        print(data.decode())
    s.close()

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    servers, clients = chatnet.discover()
    print(servers)
    s.connect((servers[0], PORT))
    recv_handler = threading.Thread(target=receiver, args=(s, ))
    recv_handler.start()
    while True:
        try:
            msg = input(">>> ")
            if msg.lower() == "/exit":
                break
            s.sendall(b"" + msg.encode())
        except KeyboardInterrupt:
            s.close()
            break

 