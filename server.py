import socket

# Create a socket object
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Define the host and port to listen on
host = 'localhost'  # Change to your server's IP address if necessary
port = 55555

# Bind the socket to the host and port
server_socket.bind((host, port))

# Listen for incoming connections
server_socket.listen(5)

print(f"Server listening on {host}:{port}")

while True:
    # Accept a connection from a client
    client_socket, addr = server_socket.accept()
    print(f"Connection from {addr}")

    # Receive data from the client
    data = client_socket.recv(1024).decode()
    if not data:
        break
    print(f"Received data: {data}")

    # Send a response back to the client
    response = "Hello, Client!"
    client_socket.send(response.encode())

    # Close the connection
    client_socket.close()
