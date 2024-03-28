import socket

IP = "10.102.85.49"
ADDR = "10.102.85.255"
PORT = 5678

msg = b"q"

def discover():
    servers = []
    clients = []
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
        s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
        s.bind((IP, PORT))
        s.sendto(msg, (ADDR, PORT))
        print("message sent yay :3")

        while True:
            resp, addr = s.recvfrom(100)
            if resp:
                if resp[0] == "s":
                    servers.append(resp[1])
                elif resp[0] == "c":
                    clients.append(resp[1])
            else:
                break
        return clients, servers
            

