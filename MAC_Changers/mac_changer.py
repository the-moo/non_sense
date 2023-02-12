#!/usr/bin/env python

#may have to run as sudo

import subprocess
#change eth0 to desired interface. Must be done for all lines!
subprocess.call("ifconfig eth0 down", shell=True)

#insert MAC address desired in line below
subprocess.call("ifconfig eth0 hw ether 00:11:22:33:44:77", shell=True)

subprocess.call("ifconfig eth0 up", shell=True)