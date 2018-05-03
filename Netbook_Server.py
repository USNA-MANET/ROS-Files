#!/usr/bin/env python

'''
-----------------------------------------------------
OBJECTIVE:
-----------------------------------------------------
The goal if this program is to provide the means to:
	- 

This process is done in three steps:
	1. Calibrate the network topogy for the 
	   turtlebot netbook
	2. Use the calibrated map to then listen and
	   potentially receive data from the 
	   workstation
	3. Read received data and execute the 
	   path provided by the workstation to then
	   from the netbook via ssh, to logon to the 
	   workstation and execute the program that
	   will then communicate to the recipiant 
	   node
-----------------------------------------------------
|||||||||||||||||||||||||||||||||||||||||||||||||||||
-----------------------------------------------------
TROUBLESHOOTING AND OPTIMIZATIONS:
-----------------------------------------------------
May want to take out the self discovery for the IP
addresses in the prepareNetbookIP() function and
instead just assign a script to each netbook with 
the name of the computer hard coded in the program
-----------------------------------------------------
|||||||||||||||||||||||||||||||||||||||||||||||||||||
-----------------------------------------------------
FUTURE IMPROVEMENTS:
-----------------------------------------------------
This program has not been vetted for security 
vulnerabilities so it may be best sometime to work
on this aspect. 

The script may be cut off when executing from the commandline so it is suggested that instead of just executing it from the workstations, rather find the file, open it, download the contents and then
once the contents are saved to the turtlebot to then execute it.
-----------------------------------------------------
|||||||||||||||||||||||||||||||||||||||||||||||||||||
-----------------------------------------------------
'''

#Imports
import paramiko
import socket
import nmap

#Variables
leonardosIP = ''
donatellosIP = ''
michelangelosIP = ''
workstationsIP = ''
netbookIP = ''

# 3.  Read data and execute from source via ssh
def processDataAndExecute(data)
	client = paramiko.SSHClient()
	client.load_system_host_keys()
	client.connect('kevin@{0}'.format(workstationsIP), password='MobileAgents')
	stdin, stdout, stderr = client.exec_command('roslaunch turtlebot_bringup minimal.launch')
	stdin, stdout, stderr = client.exec_command("gnome-terminal -x bash -c 'python {0}'; exec $SHELL".format(data)) #Opens a new terminal and executes the script
	
	Execute(data)

# 2. Receive transmitted data
def receive():
	host = netbookIP
	port = 80
	
	s = socket.socket()
	s.bind((host, port))

	s.listen(1)
	c, addr = s.accept()

	while True:
		#Needs to be always listening 
		data = c.recv(1024)
		processData(data)
		break

	c.close()

# 1. Prepare and interpret variable definitions	
def prepareNetbookIP():
	global leonardosIP
	global donatellosIP
	global michelangelosIP
	global workstationsIP 

	increment = 0

	DNR = [host_1, host_2, host_3, host_4]
	names = ['leonardo', 'donatello', 'michelangelo'] 

	nm = nmap.PortScanner()
	nm.scan('192.168.0.100', '11311') #These scans initialize these IP Addresses so they can be stored to host_1 - 4
	nm.scan('192.168.0.101', '11311')
	nm.scan('192.168.0.102', '11311')
	nm.scan('192.168.0.103', '11311')

	host_1 = nm['192.168.0.100'].hostname()
	host_2 = nm['192.168.0.101'].hostname()
	host_3 = nm['192.168.0.102'].hostname()
	host_4 = nm['192.168.0.103'].hostname()
	
	for host in DNR:
		while True:
			if host == names[increment]:
				if increment == 0: #leonardo
					if host == host_1: 
						leonardosIP = '192.168.0.100'
						return False
					if host == host_2:
						leonardosIP = '192.168.0.101'
						return False
					if host == host_3:
						leonardosIP = '192.168.0.102'
						return False
					if host == host_4:
						leonardosIP = '192.168.0.103'
						return False 

				if increment == 1: #donatello
					if host == host_1: 
						donatellosIP = '192.168.0.100'
						return False
					if host == host_2:
						donatellosIP = '192.168.0.101'
						return False
					if host == host_3:
						donatellosIP = '192.168.0.102'
						return False
					if host == host_4:
						donatellosIP = '192.168.0.103'
						return False 

				if increment == 2: #michelangelo
					if host == host_1: 
						michelangelosIP = '192.168.0.100'
						return False
					if host == host_2:
						michelangelosIP = '192.168.0.101'
						return False
					if host == host_3:
						michelangelosIP = '192.168.0.102'
						return False
					if host == host_4:
						michelangelosIP = '192.168.0.103'
						return False 

			else: #This addresses if the workstation's IP comes up
				if host == host_1:
					workstaionsIP = '192.168.0.100'
				if host == host_2:
					workstaionsIP = '192.168.0.101'
				if host == host_3:
					workstaionsIP = '192.168.0.102'
				if host == host_4:
					workstaionsIP = '192.168.0.103'
				return False

		increment += 1

	nm.scan('127.0.0.1', '11311')
	self_IP = nm['127.0.0.1'].hostname() #Discovering the IP of the turtlebot
	self_IP = self_IP.lower() 

	if self_IP == 'leonardo':
		netbookIP = leonardosIP
	if self_IP == 'donatello':
		netbookIP = donatellosIP
	if self_IP == 'michelangelo':
		netbookIP = michelangelosIP
	receive()


if __name__ == '__main__':
	prepareNetbookIP()
