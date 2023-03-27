#!/usr/bin/env python
# A basic network scanner with hard coded IP addresses

import scapy.all as scapy

def scan (ip):
    arp_request = scapy.ARP(pdst=ip)
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    print(broadcast.summary())
    
scan("172.16.5.1")
