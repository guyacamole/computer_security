import os
import time
import re


def get_machine_ip():
  # Execute the command to get IP configuration details
  result = os.popen('ipconfig').read()
  # Use regular expression to find the IPv4 Address
  ip_address_match = re.search(r'IPv4 Address[ .:]+([\d.]+)', result)
  if ip_address_match:
    return ip_address_match.group(1)
  return None


def get_default_gateway():
  # Execute the command to get IP configuration details
  result = os.popen('ipconfig').read()
  # Use regular expression to find the Default Gateway
  gateway_match = re.search(r'Default Gateway[ .:]+([\d.]+)', result)
  if gateway_match:
    return gateway_match.group(1)
  return None


def get_arp_table():
  gateway_ip = get_default_gateway()
  if not gateway_ip:
    print("Default gateway not found.")
    return []
  arp_result = os.popen(f'arp -a {gateway_ip}').read()
  arp_lines = arp_result.split('\n')
  arp_table = []
  for line in arp_lines:
    parts = line.split()
    if len(parts) == 3 and re.match(r'[\d.]+', parts[0]):
      arp_table.append({'ip': parts[0], 'mac': parts[1]})
  return arp_table


def detect_arp_changes():
  machine_ip = get_machine_ip()
  print(f"Machine IP: {machine_ip}")
  initial_arp_table = [
      entry for entry in get_arp_table() if entry['ip'] == machine_ip]
  print("Initial ARP table:")
  for entry in initial_arp_table:
    print(f"IP={entry['ip']}, MAC={entry['mac']}")
  print('debug ..')

  while True:
    time.sleep(5)
    current_arp_table = [
        entry for entry in get_arp_table() if entry['ip'] == machine_ip]

    for entry in current_arp_table:
      if entry not in initial_arp_table:
        print(f"Change detected for this machine: IP={
              entry['ip']}, MAC={entry['mac']}")
        initial_arp_table = current_arp_table

    initial_arp_table = current_arp_table


detect_arp_changes()
