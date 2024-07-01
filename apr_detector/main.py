import re
import time
import platform
import os


def run_command(command):
  # Function to run a command and return its output
  stream = os.popen(command)
  result = stream.read()
  return result


def get_machine_ip():
  if platform.system() == "Windows":
    result = run_command('ipconfig')
    ip_addresses = re.findall(r'IPv4 Address. *: ([\d.]+)', result)
  else:
    result = run_command('hostname -I')
    ip_addresses = result.split()
  machine_ip = ip_addresses[0] if ip_addresses else None
  print(f"Machine IP: {machine_ip if machine_ip else 'Not Found'}")
  return machine_ip


def get_arp_table():
  if platform.system() == "Windows":
    arp_result = run_command(
        'Get-NetNeighbor -AddressFamily IPv4 | Select-Object IPAddress,LinkLayerAddress')
  else:
    arp_result = run_command('arp -a')
  print(f"ARP command result: {arp_result}")  # Debugging print statement
  arp_table = []
  if platform.system() == "Windows":
    for line in arp_result.split('\n'):
      parts = line.split()
      if len(parts) >= 2 and re.match(r'[\d.]+', parts[0]):
        arp_table.append({'ip': parts[0], 'mac': parts[1]})
  else:
    arp_lines = arp_result.split('\n')
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
