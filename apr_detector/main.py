import scapy.all as scapy
router_ip = "192.168.122.1"

# Obtener la dirección MAC del router
mac_router = scapy.ARP().whohas(router_ip)[0][1]

# Verificar si la dirección MAC del router en la tabla ARP coincide con la real
mac_router_en_arp = scapy.ARP().whohas(router_ip)[0][1]

if mac_router_en_arp == mac_router:
    print("La tabla ARP no ha sido modificada.")
else:
    print("¡La tabla ARP ha sido modificada! Posible ataque ARP Spoofing.")
