from scapy.all import ARP, Ether, srp
import time


def get_mac(ip):
  arp_request = ARP(pdst=ip)
  broadcast = Ether(dst="ff:ff:ff:ff:ff:ff")
  arp_request_broadcast = broadcast/arp_request
  answered_list = srp(arp_request_broadcast, timeout=1, verbose=False)[0]
  return answered_list[0][1].hwsrc if answered_list else None


def detect_arp_spoofing(gateway_ip, original_mac):
  while True:
    current_mac = get_mac(gateway_ip)
    if current_mac and current_mac != original_mac:
      print(f"[!] ARP Spoofing detected! Original MAC: {original_mac}, New MAC: {current_mac}")
    else:
      print("No ARP Spoofing detected.")
    time.sleep(5)


if __name__ == "__main__":
  gateway_ip = input("Enter the IP address of the router: ")
  original_mac = get_mac(gateway_ip)

  if not original_mac:
    print("Could not find the original MAC address for the router.")
  else:
    detect_arp_spoofing(gateway_ip, original_mac)
