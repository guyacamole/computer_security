import os
import re
import time


def get_machine_ip():
  # Using hostname -I to get the machine IP, taking the first IP as the machine IP
  result = os.popen('hostname -I').read().strip()
  ip_addresses = result.split()
  machine_ip = ip_addresses[0] if ip_addresses else None
  print(f"Machine IP: {machine_ip if machine_ip else 'Not Found'}")
  return machine_ip


def get_default_gateway():
  # Using ip route to get the default gateway
  result = os.popen('ip route show default').read()
  gateway_match = re.search(r'default via ([\d.]+)', result)
  default_gateway = gateway_match.group(1) if gateway_match else None
  print(f"Default Gateway: {default_gateway if default_gateway else 'Not Found'}")
  return default_gateway


def get_arp_table():
  gateway_ip = get_default_gateway()
  if not gateway_ip:
    print("Default gateway not found.")
    return []
  arp_result = os.popen('arp -a').read()
  print(f"ARP command result: {arp_result}")  # Debugging print statement
  arp_lines = arp_result.split('\n')
  arp_table = []
  for line in arp_lines:
    parts = line.split()
    if len(parts) >= 4 and re.match(r'[\d.]+', parts[1].strip('()')):
      arp_table.append({'ip': parts[1].strip('()'), 'mac': parts[3]})
  print(f"ARP Table: {arp_table}")
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
        print(f"Change detected for this machine: IP={entry['ip']}, MAC={entry['mac']}")
        initial_arp_table = current_arp_table

    initial_arp_table = current_arp_table


detect_arp_changes()
