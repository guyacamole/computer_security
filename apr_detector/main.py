import os
import re


def get_machine_ip():
  result = os.popen('ip addr').read()
  ip_address_match = re.search(r'inet ([\d.]+)/', result)
  print(f"Machine IP: {ip_address_match.group(
      1) if ip_address_match else 'Not Found'}")
  return ip_address_match.group(1) if ip_address_match else None


def get_arp_table():
  arp_result = os.popen('arp -a').read()
  print(f"ARP command result: {arp_result}")  # Debugging print statement
  arp_lines = arp_result.split('\n')
  arp_table = []
  for line in arp_lines:
    parts = line.split()
    if len(parts) >= 4 and re.match(r'[\d.]+', parts[1].strip('()')):
      arp_table.append({'ip': parts[1].strip('()'), 'mac': parts[3]})
  return arp_table


def check_host_arp():
  machine_ip = get_machine_ip()
  if not machine_ip:
    print("Machine IP not found. Exiting.")
    return

  arp_table = get_arp_table()
  host_arp_entry = next(
      (entry for entry in arp_table if entry['ip'] == machine_ip), None)

  if host_arp_entry:
    print(f"Host ARP entry: IP={host_arp_entry['ip']}, MAC={
          host_arp_entry['mac']}")
  else:
    print("No ARP entry found for the host machine.")


check_host_arp()
