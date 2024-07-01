from scapy.all import ARP, Ether, srp, conf
import time

# Set the network interface
conf.iface = "enp1s0"


def get_arp_table():
  arp = ARP(pdst="192.168.122.1/24")
  ether = Ether(dst="ff:ff:ff:ff:ff:ff")
  packet = ether/arp
  result = srp(packet, timeout=3, verbose=0)[0]
  arp_table = []
  for sent, received in result:
    arp_table.append({'ip': received.psrc, 'mac': received.hwsrc})
  return arp_table


def detect_arp_spoofing(arp_table, arp_history):
  ip_mac_mapping = {}
  for entry in arp_table:
    ip, mac = entry['ip'], entry['mac']
    if mac in ip_mac_mapping and ip_mac_mapping[mac] != ip:
      print(f"ARP Spoofing Detected: MAC address {mac} is associated with multiple IPs: {ip_mac_mapping[mac]} and {ip}.")
    if ip in ip_mac_mapping.values() and mac not in ip_mac_mapping:
      print(f"ARP Spoofing Detected: IP address {ip} is associated with multiple MACs: {list(ip_mac_mapping.keys())[list(ip_mac_mapping.values()).index(ip)]} and {mac}.")
    ip_mac_mapping[mac] = ip

  # Check for frequent changes in IP-MAC mappings
  for history_table in arp_history:
    for entry in arp_table:
      if entry in history_table and entry['mac'] != history_table[entry['ip']]:
        print(f"Potential ARP Spoofing: IP {entry['ip']} has changed MAC from {
              history_table[entry['ip']]} to {entry['mac']}.")


def detect_arp_changes():
  arp_history = []
  initial_arp_table = get_arp_table()
  print("Initial ARP table:", initial_arp_table)
  # Initial check for ARP spoofing
  detect_arp_spoofing(initial_arp_table, arp_history)

  while True:
    time.sleep(5)  # Wait for 5 seconds before checking again
    current_arp_table = get_arp_table()
    print("Current ARP table:", current_arp_table)
    detect_arp_spoofing(current_arp_table, arp_history)

    # Update ARP history
    arp_history.append({entry['ip']: entry['mac']
                       for entry in current_arp_table})
    if len(arp_history) > 5:  # Keep the last 5 ARP tables
      arp_history.pop(0)


if __name__ == "__main__":
  detect_arp_changes()
