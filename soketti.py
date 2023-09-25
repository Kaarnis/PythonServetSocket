import socket

# Create a socket object
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Define the server's host and port
server_host = 'localhost'  # Change to the server's IP address if necessary
server_port = 55555

# Connect to the server
client_socket.connect((server_host, server_port))

# Send data to the server
message = "Hello, Server!"
client_socket.send(message.encode())

# Receive the server's response
response = client_socket.recv(1024).decode()
print(f"Server response: {response}")

# Close the client socket
client_socket.close()
