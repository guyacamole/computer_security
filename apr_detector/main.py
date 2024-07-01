from scapy.all import ARP, Ether, srp, conf
import time

# Set the network interface (replace 'eth0' with your interface)
conf.iface = "wlp0s20f3"


def get_arp_table():
  arp = ARP(pdst="192.168.0.1/24")
  ether = Ether(dst="ff:ff:ff:ff:ff:ff")
  packet = ether/arp
  result = srp(packet, timeout=3, verbose=0)[0]
  arp_table = []
  for sent, received in result:
    arp_table.append({'ip': received.psrc, 'mac': received.hwsrc})
  return arp_table


def detect_arp_spoofing(arp_table):
  ip_mac_mapping = {}
  for entry in arp_table:
    ip, mac = entry['ip'], entry['mac']
    if mac in ip_mac_mapping and ip_mac_mapping[mac] != ip:
      print(f"ARP Spoofing Detected: MAC address {mac} is associated with multiple IPs: {ip_mac_mapping[mac]} and {ip}.")
    if ip in ip_mac_mapping.values() and mac not in ip_mac_mapping:
      print(f"ARP Spoofing Detected: IP address {ip} is associated with multiple MACs: {list(ip_mac_mapping.keys())[list(ip_mac_mapping.values()).index(ip)]} and {mac}.")
    ip_mac_mapping[mac] = ip


def detect_arp_changes():
  initial_arp_table = get_arp_table()
  print("Initial ARP table:", initial_arp_table)
  detect_arp_spoofing(initial_arp_table)  # Initial check for ARP spoofing

  while True:
    time.sleep(5)  # Wait for 5 seconds before checking again
    current_arp_table = get_arp_table()
    print("Current ARP table:", current_arp_table)
    # Check for ARP spoofing in the current ARP table
    detect_arp_spoofing(current_arp_table)

    # Detect new or removed devices (optional, based on your requirements)
    for entry in current_arp_table:
      if entry not in initial_arp_table:
        print(f"New device detected: IP={entry['ip']}, MAC={entry['mac']}")
    for entry in initial_arp_table:
      if entry not in current_arp_table:
        print(f"Device removed: IP={entry['ip']}, MAC={entry['mac']}")

    initial_arp_table = current_arp_table


# Run the script
if __name__ == "__main__":
  detect_arp_changes()
