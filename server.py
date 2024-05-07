import socket
import threading

PORT = 5678

def client_handler(conn):
    while True:
        data = conn.recv(1024)
        if not data:
            break
        print(data.decode())

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind(("192.168.1.20", PORT))
    s.listen()
    print(f"Listening on port {PORT}")

    while True:
        conn, addr = s.accept()
        print(f"{addr} connected")
        handle_client = threading.Thread(target=client_handler, args=(conn, ))
        handle_client.start()