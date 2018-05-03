#!/usr/bin/python

import socket

s = socket.socket()
port = 12345
# '' makes the server listen to requests 
# coming from other computers on the network
s.bind(('', port))

s.listen(5)

c, addr = s.accept()
print 'Got connection from', addr
temp = raw_input('Type anything: ')
c.send(temp)
c.close()
