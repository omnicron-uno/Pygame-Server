# server.py
import socket
import threading

HOST = '0.0.0.0'
PORT = 10000

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen()

clients = []

def handle_client(conn, addr):
    print(f"[NEW] {addr} connected.")
    while True:
        try:
            data = conn.recv(1024)
            if not data:
                break
            print(f"[RECV from {addr}] {data.decode()}")
            for c in clients:
                if c != conn:
                    c.sendall(data)
        except:
            break
    conn.close()
    clients.remove(conn)
    print(f"[DISCONNECT] {addr} disconnected.")

print(f"[LISTENING] on {PORT}")
while True:
    conn, addr = server.accept()
    clients.append(conn)
    threading.Thread(target=handle_client, args=(conn, addr)).start()
