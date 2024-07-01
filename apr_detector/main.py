import os
import time
import psutil
import socket


def get_ip_addresses():
  ip_info = {}
  for interface, addrs in psutil.net_if_addrs().items():
    for addr in addrs:
      if addr.family == socket.AF_INET:
        ip_info[interface] = addr.address
  return ip_info


def get_default_gateway():
  # Use netstat to get the default gateway
  result = os.popen('netstat -rn').read()
  for line in result.split('\n'):
    if line.startswith('  0.0.0.0'):
      parts = line.split()
      if len(parts) >= 2:
        return parts[1]
  return None


def main():
  # Initial network information
  ip_info = get_ip_addresses()
  default_gateway = get_default_gateway()

  print("Initial IP info:", ip_info)
  print("Initial Default gateway:", default_gateway)
  print("Monitoring network information for changes...")

  while True:
    time.sleep(2)  # Check every 10 seconds

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
