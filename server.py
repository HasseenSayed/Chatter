import socket

def handle_client(conn, addr):
    while True:
        data = conn.recv(1024)
        conn.sendall(b"Received")

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((socket.gethostname(), 5678))
    s.listen()
    conn, addr = s.accept()
    handle_client(conn, addr)

    while True:
        data = conn.recv(1024)
        if not data:
            break
        conn.sendall("Yo bro\n")