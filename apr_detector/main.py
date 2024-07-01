import os
import time
import re


def get_machine_ip():
  result = os.popen('ip addr').read()
  ip_address_match = re.search(r'inet ([\d.]+)/', result)
  print(f"Machine IP: {ip_address_match.group(
      1) if ip_address_match else 'Not Found'}")
  if ip_address_match:
    return ip_address_match.group(1)
  return None


def get_default_gateway():
  result = os.popen('ip route').read()
  gateway_match = re.search(r'default via ([\d.]+)', result)
  print(f"Default Gateway: {gateway_match.group(
      1) if gateway_match else 'Not Found'}")
  if gateway_match:
    return gateway_match.group(1)
  return None


def get_arp_table():
  arp_result = os.popen('arp -a').read()
  arp_lines = arp_result.split('\n')
  arp_table = []
  for line in arp_lines:
    parts = line.split()
    if len(parts) >= 4 and re.match(r'[\d.]+', parts[1].strip('()')):
      arp_table.append({'ip': parts[1].strip('()'), 'mac': parts[3]})
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
