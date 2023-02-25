#!/usr/bin/env python
# A basic network scanner with hard coded IP addresses

import scapy.all as scapy

def scan (ip):
    scapy.arping(ip)

scan("172.16.5.1") #Put IP or subnet to scan here
