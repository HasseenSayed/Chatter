import socket
import threading

PORT = 5678

conns = []

def client_handler(conn, addr):
    while True:
        data = conn.recv(1024)
        if not data:
            print(f"{addr[0]} left the chat")
            break
        print(data.decode())
        for con in conns:
            con.sendall(data)
    conn.close()

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind(("localhost", PORT))
    s.listen()
    print(f"Listening on port {PORT}")
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as temp:
        query, addr = temp.recvfrom(1024)
        if query.decode() == "q":
            temp.sendto("s".encode, addr)
    if start[0] == b"q":
        s.connect(start[1])
        s.sendto("s", (start[1], PORT))
    while True:
        try:
            conn, addr = s.accept()
            print(f"{addr[0]} connected")
            conns.append(conn)
            handle_client = threading.Thread(target=client_handler, args=(conn, addr))
            handle_client.start()
        except:
            print("Closing server...")
            s.close()
            break