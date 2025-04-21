import socket

# Server setup
host = '0.0.0.0'  # Listen on all interfaces (Render will use the public IP)
port = 10000       # Port number (make sure this matches the one you selected on Render)

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((host, port))
server_socket.listen(5)

print(f"Server listening on port {port}...")

# Wait for clients to connect
while True:
    client_socket, client_address = server_socket.accept()
    print(f"Connection from {client_address}")

    # Send a welcome message to the client
    client_socket.send(b"Welcome to the Pygame server!")

    # Handle the client's requests (this can be modified based on your game's logic)
    data = client_socket.recv(1024)
    print(f"Received from client: {data.decode()}")

    # Respond to the client
    client_socket.send(b"Thanks for connecting!")

    # Close the connection after handling the request
    client_socket.close()
