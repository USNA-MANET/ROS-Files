#!/usr/bin/python

import socket

# TCP connection
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# splinter's IP and decided upon port
host = "192.168.0.100"
port = 12345+3

s.connect((host, port))
print s.recv(1024)
s.close

exit()
