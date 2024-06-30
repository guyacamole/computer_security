from scapy.all import ARP, Ether, srp


def get_arp_table():
  # Create an ARP request packet
  arp = ARP(pdst="192.168.0.1/24")
  ether = Ether(dst="ff:ff:ff:ff:ff:ff")
  packet = ether/arp

  # Send the packet and capture the response
  result = srp(packet, timeout=3, verbose=0)[0]

  # Extract the ARP table from the response
  arp_table = []
  for sent, received in result:
    arp_table.append({'ip': received.psrc, 'mac': received.hwsrc})

  return arp_table


def detect_arp_changes():
  # Get the initial ARP table
  initial_arp_table = get_arp_table()

  while True:
    # Get the current ARP table
    current_arp_table = get_arp_table()

    # Compare the current ARP table with the initial ARP table
    for entry in current_arp_table:
      if entry not in initial_arp_table:
        print(f"New device detected: IP={entry['ip']}, MAC={entry['mac']}")

    for entry in initial_arp_table:
      if entry not in current_arp_table:
        print(f"Device removed: IP={entry['ip']}, MAC={entry['mac']}")

    # Update the initial ARP table
    initial_arp_table = current_arp_table


# Run the script
detect_arp_changes()
