#!/usr/bin/env python
# A basic network scanner with user input and parsed results that go into a pretty chart output


import scapy.all as scapy

target=input("IP Address to scan: ") #IP to scan

def scan (ip):
    arp_request = scapy.ARP(pdst=ip)
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_request_broadcast = broadcast/arp_request
    answered_list = scapy.srp(arp_request_broadcast, timeout=1, verbose=False)[0]

    print("IP\t\t\tMAC Address\n----------------------------------------------------")#\t prints tab
    for element in answered_list:
        print(element[1].psrc + "\t\t" +element[1].hwsrc)

scan(target) #IP address to be scanned
