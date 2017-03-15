#!/usr/bin/python
from scapy.all import *
import sys

def queryForDNS(pkt):
    if IP in pkt:
        #print(pkt)
        ip_src = pkt[IP].src
        ip_dst = pkt[IP].dst
        if pkt.haslayer(DNS) and pkt.getlayer(DNS).qr == 0:
            print ("Source :" + str(ip_src) + "Destination : " + str(ip_dst) + pkt.getLayer(DNS).qd.qname)

def queryForFTP(pkt):
    if pkt.haslayer(TCP) and pkt.haslayer(Raw):
        if pkt[TCP].sport == 21 or pkt[TCP].dport == 21:
            print ("Source :" + str(ip_src) + "Destination : " + str(ip_dst) + "FTP Detected")




sniff(filter = "port 53",prn=queryForDNS,store=0)
sniff(prn=queryForFTP,store=0)



