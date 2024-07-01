import os
import scapy.all as scapy
import time

# Check for root privileges
if not os.geteuid() == 0:
  exit("This script requires root privileges. Run it again with sudo.")


def get_mac(ip):
  arp_request = scapy.ARP(pdst=ip)
  broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
  arp_request_broadcast = broadcast / arp_request
  answered_list = scapy.srp(arp_request_broadcast, timeout=1, verbose=False)[0]
  return answered_list[0][1].hwsrc


def restore(target_ip, spoof_ip):
  target_mac = get_mac(target_ip)
  spoof_mac = get_mac(spoof_ip)
  packet = scapy.ARP(op=2, pdst=target_ip, hwdst=target_mac,
                     psrc=spoof_ip, hwsrc=spoof_mac)
  # Send a few packets to ensure the ARP table is updated
  scapy.send(packet, count=4, verbose=False)


target_ip = "192.168.122.178"  # IP of the target machine
gateway_ip = "192.168.122.1"  # IP of the router

try:
  print("Restoring ARP tables...")
  while True:
    restore(target_ip, gateway_ip)
    restore(gateway_ip, target_ip)
    time.sleep(2)  # Add delay to avoid flooding the network
except KeyboardInterrupt:
  print("\nARP tables restored to their correct state.")
