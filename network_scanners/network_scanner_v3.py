#!/usr/bin/env python
# A basic network scanner with hard coded IP addresses and IPv4 broadcast


import scapy.all as scapy

def scan (ip):
    arp_request = scapy.ARP(pdst=ip)
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_request_broadcast = broadcast/arp_request
    print (arp_request_broadcast.summary())
    arp_request_broadcast.show()
    
scan("172.16.5.1") #IP address to be scanned
