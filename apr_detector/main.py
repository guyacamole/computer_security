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
  # Use ipconfig to get the default gateway
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


def main():
  # Initial network information
  ip_info = get_ip_addresses()
  default_gateway = get_default_gateway()

  print("Initial IP info:", ip_info)
  print("Initial Default gateway:", default_gateway)
  print("Monitoring network information for changes...")

  while True:
    time.sleep(10)  # Check every 10 seconds

    # Get the current network information
    current_ip_info = get_ip_addresses()
    current_default_gateway = get_default_gateway()

    # Compare IP addresses
    if current_ip_info != ip_info:
      print("IP addresses have changed!")
      print("Old IP info:", ip_info)
      print("New IP info:", current_ip_info)
      ip_info = current_ip_info

    # Compare default gateway
    if current_default_gateway != default_gateway:
      print("Default gateway has changed!")
      print("Old gateway:", default_gateway)
      print("New gateway:", current_default_gateway)
      default_gateway = current_default_gateway


if __name__ == "__main__":
  main()
