import os
import re
import subprocess


def get_default_gateway():
  result = os.popen('ipconfig').read()
  gateway_match = re.search(r'Default Gateway[ .:]*([\d.]+)', result)
  if gateway_match:
    return gateway_match.group(1)
  return None


def ping_ip(ip_address):
  # Ping the IP address to ensure it's in the ARP table
  subprocess.run(['ping', '-c', '1', ip_address], stdout=subprocess.DEVNULL)


def get_arp_table():
  gateway_ip = get_default_gateway()
  if not gateway_ip:
    print("Default gateway not found.")
    return []
  # Ping the default gateway to ensure its ARP entry exists
  ping_ip(gateway_ip)
  arp_result = os.popen(f'arp -a {gateway_ip}').read()
  if "no ARP Entries Found" in arp_result:
    print("No ARP entries found after ping. Check network connectivity.")
    return []
  arp_lines = arp_result.split('\n')
  arp_table = []
  for line in arp_lines:
    parts = line.split()
    if len(parts) == 3 and re.match(r'[\d.]+', parts[0]):
      arp_table.append({'ip': parts[0], 'mac': parts[1]})
  return arp_table


# Example usage
arp_table = get_arp_table()
print(f"ARP Table: {arp_table}")
