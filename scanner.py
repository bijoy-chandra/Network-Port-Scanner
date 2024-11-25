#!/bin/python
# Port scanning tool: It will scan the host and look out for which ports are open

import sys
import socket
from datetime import datetime

# Define our target

if len(sys.argv) == 2:
	target = socket.gethostbyname(sys.argv[1])
else:
	print("Invalid amount of arguments.")
	print("Syntax: python3 scanner.py <ip>")
	sys.exit()

# Add a Banner

print("_" * 50)
print("Scanning target "+ target)
print("Time Started: " + str(datetime.now()))
print("_" * 50)

try:
	for port in range (1, 100):
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		socket.setdefaulttimeout(1)
		result = s.connect_ex((target, port))
		if result == 0:
			print("port {} is open".format(port))
		s.close()

except KeyboardInterrupt:
	print("\nExisting program.")
	sys.exit()
except socket.gaierror:
	print("Hostname could not be resolved.")
	sys.exit()
except socket.error:
	print("Couldn't connect to the server.")
	sys.exit()
