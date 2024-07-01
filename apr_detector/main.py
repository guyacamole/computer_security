from scapy.all import arpcache, arping, Ether


def get_mac(ip):
  # Enviar una solicitud ARP para obtener la dirección MAC de una IP
  ans, _ = arping(ip, timeout=2, verbose=False)
  for s, r in ans:
    return r[Ether].src
  return None


def check_arp_table(router_ip, known_router_mac):
  # Obtener la tabla ARP del sistema
  arp_table = arpcache()
  current_router_mac = arp_table.get(router_ip)
  if current_router_mac is None:
    print("No se encontró la IP del router en la tabla ARP.")
    return False
  if current_router_mac.lower() != known_router_mac.lower():
    print(f"Alerta: La dirección MAC del router ha cambiado a {current_router_mac}")
    return False
  else:
    print("La tabla ARP no ha sido modificada.")
    return True


if __name__ == "__main__":

  router_ip = '192.168.122.1'
  known_router_mac = '52:54:00:b7:ca:05'

  if check_arp_table(router_ip, known_router_mac):
    print("No se detectaron modificaciones en la tabla ARP.")
  else:
    print("Se detectaron modificaciones en la tabla ARP.")
