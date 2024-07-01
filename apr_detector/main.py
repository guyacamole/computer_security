import os
import time
import psutil
import socket
import re


def get_ip_addresses():
  ip_info = {}
  for interface, addrs in psutil.net_if_addrs().items():
    for addr in addrs:
      if addr.family == socket.AF_INET:
        ip_info[interface] = addr.address
  return ip_info


def get_default_gateway():
  result = os.popen('ipconfig').read()
  gateway = None
  found_gateway = False
  for line in result.split('\n'):
    if 'Default Gateway' in line:
      found_gateway = True
    elif found_gateway:
      parts = line.strip().split()
      if len(parts) > 0 and re.match(r'^\d{1,3}(\.\d{1,3}){3}$', parts[0]):
        gateway = parts[0]
        break
      found_gateway = False
  return gateway


def get_arp_table():
  result = os.popen('arp -a').read()
  arp_table = []
  for line in result.split('\n'):
    if line.strip() and line.startswith('  '):
      parts = line.split()
      if len(parts) >= 3:
        arp_table.append((parts[0], parts[1], parts[2]))
  return arp_table


def main():
  ip_info = get_ip_addresses()
  default_gateway = get_default_gateway()
  arp_table = get_arp_table()

  print("Initial IP info:", ip_info)
  print("Initial Default gateway:", default_gateway)
  print("Initial ARP table:", arp_table)
  print("Monitoring network information for changes...")

  while True:
    time.sleep(1)  # Check every 10 seconds

    current_ip_info = get_ip_addresses()
    current_default_gateway = get_default_gateway()
    current_arp_table = get_arp_table()

    if current_ip_info != ip_info:
      print("IP addresses have changed!")
      print("Old IP info:", ip_info)
      print("New IP info:", current_ip_info)
      ip_info = current_ip_info

    if current_default_gateway != default_gateway:
      print("Default gateway has changed!")
      print("Old gateway:", default_gateway)
      print("New gateway:", current_default_gateway)
      default_gateway = current_default_gateway

    if current_arp_table != arp_table:
      print("ARP table has changed!")
      print("Old ARP table:", arp_table)
      print("New ARP table:", current_arp_table)
      arp_table = current_arp_table


if __name__ == "__main__":
  main()
