# Sending UDP Packets with Python: A Practical Guide

---


```py
# Send data via udp

import socket

UDP_IP = "127.0.0.1"  # Target IP address
UDP_PORT = 12345       # Target port number

message = b"Hello UDP!"  # The message to send, as bytes

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # Create a UDP socket

sock.sendto(message, (UDP_IP, UDP_PORT))  # Send the UDP packet

print(f"Sent message to {UDP_IP}:{UDP_PORT}")
```

