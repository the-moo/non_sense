#!/usr/bin/env python
# A basic network scanner with a timeout feature and parsed results


import scapy.all as scapy


def scan (ip):
    arp_request = scapy.ARP(pdst=ip)
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_request_broadcast = broadcast/arp_request
    answered_list = scapy.srp(arp_request_broadcast, timeout=1)[0]
   
    for element in answered_list:
        print(element[1].psrc)
        print(element[1].hwsrc)
        print("----------------------------------------------------")


scan("172.16.5.1/24") #IP address to be scanned
