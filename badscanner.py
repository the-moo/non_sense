#/bin/python3

"""
A poorly made port scanner that scans runs very slowly.
Currently limited to ports 50-85 to save time.  See line 26 to adjust range.
"""

import sys
import socket
from datetime import datetime

#Define our target
if len(sys.argv) == 2:
    target=socket.gethostbyname(sys.argv[1]) #Translate hostname to IPv4
else:
    print("Invalid amount of arguments.")
    print("Syntax: pyhton3 badscanner.py <ip>")

#ADD A PRETTY BANNER
print("-"*50)
print("Scanning target: " +target)
print("Time started: " +str(datetime.now()))
print("-"*50)

try:
    for port in range(50,85): #Range of ports to scan 1-65535
        s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)
        result = s.connect_ex((target,port))
        if result == 0:
            print (f"Port {port} is open")
        s.close()

except KeyboardInterrupt: #allows stopping of program with ctl C
    print("\nExiting program.")
    sys.exit()

except socket.gaierror:
    print ("Hostname could not be resolved.")
    sys.exit()

except socket.error:
    print("Could not connect to the server.")
    sys.exit()
    