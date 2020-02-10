import socket

UDP_IP = "192.168.1.238"
UDP_PORT = 5005
MESSAGE = "Hello, World!"

sock = socket.socket(socket.AF_INET, # Internet
                      socket.SOCK_DGRAM) # UDP
sock.sendto(MESSAGE.encode(), (UDP_IP, UDP_PORT))
