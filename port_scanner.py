'''
Port Scanner - Enter an IP address and a port range where the program will then attempt to find open ports on the given computer by connecting to each of them. 
On any successful connections mark the port as open.

Solution adapted and edited from https://www.pythonforbeginners.com/code-snippets-source-code/port-scanner-in-python
Converted to Python 3 and improved

**Prob your own IP for open ports**
'''

#!/usr/bin/env python
import socket
import subprocess
import sys
from datetime import datetime

# Clear the screen
subprocess.call('clear', shell=True)

# Ask for input
while True:
	
	try:
		remoteServer    = input("Enter a remote host (IPv4) to scan: ")
		remoteServerIP  = socket.gethostbyname(remoteServer)
		port_range1    = input("Enter a port range to scan from: ")
		port_range2    = input("Enter a port range to scan to: ")
	except socket.gaierror:
	    print('Hostname could not be resolved. Try again')
	    continue
	else:
		break

# Print a nice banner with information on which host we are about to scan
print("-" * 60)
print("Please wait, scanning remote host", remoteServerIP)
print("Press <Ctrl+C> to exit scanning and program")
print("-" * 60)

# Check what time the scan started
t1 = datetime.now()

# We also put in some error handling for catching errors

try:
    for port in range(int(port_range1), int(port_range2)):  
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        result = sock.connect_ex((remoteServerIP, port))
        if result == 0:
            print("Port {}: 	 Open".format(port))
        sock.close()

except KeyboardInterrupt:
    print("You pressed Ctrl+C")
    sys.exit()

except socket.gaierror:
    print('Hostname could not be resolved. Exiting')
    sys.exit()

except socket.error:
    print("Couldn't connect to server")
    sys.exit()

# Checking the time again
t2 = datetime.now()

# Calculates the difference of time, to see how long it took to run the script
total =  t2 - t1

# Printing the information to screen
print('Scanning Completed in: ', total)


