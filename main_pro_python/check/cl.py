import socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(('127.0.0.1', 5000))
## Send some data, this method can be called multiple times
sock.send("bye shihab")
## Receive up to 4096 bytes from a peer
# sock.recv(4096)
## Close the socket connection, no more data transmission
sock.close()
