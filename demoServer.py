#!/usr/bin/python

import socket

#make sockets for Michelangelo, Leonardo, & Donatello
#sD = socket.socket()
sL = socket.socket()
sM = socket.socket()
sR = socket.socket()

#Allow reuse
#sD.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,1)
sL.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,1)
sM.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,1)
sR.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,1)

#start port for sockets
port = 12345

# '' makes the server listen to requests 
# coming from other computers on the network
#sD.bind(('', port))
sL.bind(('', port+1))
sM.bind(('', port+2))
sR.bind(('', port+3))

#create sockets to listen to to requests 
#sD.listen(5)
sL.listen(5)
sM.listen(5)
sR.listen(5)

#accept all three connections before asking prompt
#cD, addrD = sD.accept()
cL, addrL = sL.accept()
cM, addrM = sM.accept()
cR, addrR = sR.accept()
#print 'Got connection from ', addrD
print 'Got conectiion from ', addrL
print 'Got connection from ', addrM
print 'Got connection from ', addrR
print 'Swarm is initialized'

#Swarmn is waiting on input to go
temp = raw_input('Type anything to begin Swarm: ')
#cD.send(temp)
cL.send(temp)
cM.send(temp)
cR.send(temp)

#end connections
#cD.close()
cL.close()
cM.close()
cR.close()

#end connections
#sD.shutdown(SHUT_RDWR)
#sL.shutdown(SHUT_RDWR)
#sM.shutdown(SHUT_RDWR)
#sD.close()
sL.close()
sM.close()
sR.close()
    

