import time
import psutil


def get_network_info():
  # Get IP addresses
  addresses = psutil.net_if_addrs()
  ip_info = {interface: addresses[interface]
             [1].address for interface in addresses if addresses[interface][1].family == psutil.AF_INET}

  # Get default gateway
  gateways = psutil.net_if_stats()
  default_gateway = psutil.net_if_addrs()[list(gateways.keys())[0]][1].address

  return ip_info, default_gateway


def main():
  # Initial network information
  ip_info, default_gateway = get_network_info()

  print("Monitoring network information for changes...")

  while True:
    time.sleep(10)  # Check every 10 seconds

    # Get the current network information
    current_ip_info, current_default_gateway = get_network_info()

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
