from scapy.all import ARP, sniff


def analyze_arp_packet(packet):
  if ARP in packet and packet[ARP].op == 2:  # Check for ARP reply (op=2)
    sender_ip = packet[ARP].psrc
    sender_mac = packet[ARP].hwsrc
    # Maintain a dictionary to track IP-MAC mappings
    arp_table = {}
    if sender_mac in arp_table and arp_table[sender_mac] != sender_ip:
      print(f"Potential ARP Spoofing Detected: MAC address {sender_mac} is associated with multiple IPs: {arp_table[sender_mac]} and {sender_ip}.")
    arp_table[sender_mac] = sender_ip


def main():
  sniff(iface="enps0", prn=analyze_arp_packet)


if __name__ == "__main__":
  main()
