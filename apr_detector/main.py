import subprocess
import re


def get_machine_ip():
  # Using PowerShell to get the IP address
  result = subprocess.run(
      ["powershell", "-Command", "Get-NetIPAddress -AddressFamily IPv4 | Where-Object { $_.InterfaceAlias -like '*Ethernet*' } | Select-Object IPAddress"], capture_output=True, text=True)
  ip_address_match = re.search(r'IPAddress\s+:\s([\d.]+)', result.stdout)
  print(f"Machine IP: {ip_address_match.group(
      1) if ip_address_match else 'Not Found'}")
  return ip_address_match.group(1) if ip_address_match else None


def get_arp_table():
  # Using PowerShell to get the ARP table
  arp_result = subprocess.run(
      ["powershell", "-Command", "Get-NetNeighbor -AddressFamily IPv4 | Select-Object IPAddress,LinkLayerAddress"], capture_output=True, text=True)
  # Debugging print statement
  print(f"ARP command result: {arp_result.stdout}")
  arp_lines = arp_result.stdout.split('\n')
  arp_table = []
  for line in arp_lines:
    if 'IPAddress' in line or '---' in line or not line.strip():
      continue  # Skip headers and empty lines
    parts = line.split()
    if len(parts) >= 2:
      arp_table.append({'ip': parts[0], 'mac': parts[1]})
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
    print(f"Host ARP entry: IP={host_arp_entry['ip']}, MAC={host_arp_entry['mac']}")
  else:
    print("No ARP entry found for the host machine.")


check_host_arp()
