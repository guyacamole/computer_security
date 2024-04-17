import nmap

def scan(host, ports, arguments, run_as_root):
  nm = nmap.PortScanner()
  ports = ",".join(ports)  # Join the list into a string
  if run_as_root:
    nm.scan(hosts=host, ports=ports, arguments=arguments + ' -O -sV --script=default', sudo=True)
  else:
    nm.scan(hosts=host, ports=ports, arguments=arguments + ' -O -sV --script=default')

  for host in nm.all_hosts():
    print(f"Host : {host} ({nm[host].hostname()})")
    print(f"State : {nm[host].state()}")
    for osmatch in nm[host]['osmatch']:
      print("----------")
      print('OsMatch.name : {0}'.format(osmatch['name']))
      print('OsMatch.accuracy : {0}'.format(osmatch['accuracy']))
      print('OsMatch.line : {0}'.format(osmatch['line']))
      for osclass in osmatch['osclass']:
        print('OsClass.type : {0}'.format(osclass['type']))
        print('OsClass.vendor : {0}'.format(osclass['vendor']))
        print('OsClass.osfamily : {0}'.format(osclass['osfamily']))
        print('OsClass.osgen : {0}'.format(osclass['osgen']))
        print('OsClass.accuracy : {0}'.format(osclass['accuracy']))
    for proto in nm[host].all_protocols():
      print("----------")
      print(f"Protocol : {proto}")
      print("----------")

      lport = nm[host][proto].keys()
      for port in lport:
        print(f"Port : {port}\tState : {nm[host][proto][port]['state']}")
        print(f"Name : {nm[host][proto][port]['name']}")
        print(f"Product : {nm[host][proto][port]['product']}")
        print(f"Version : {nm[host][proto][port]['version']}")
        print(f"Extra info : {nm[host][proto][port]['extrainfo']}")
        print(f"Conf : {nm[host][proto][port]['conf']}")
        print(f"Cpe : {nm[host][proto][port]['cpe']}")
        print("----------")

# Example usage
host = input("Enter the host: ")
ports = input("Enter the ports (comma-separated): ").split(",")
arguments = input("Enter the arguments: ")
run_as_root = input("Run as root? (y/n): ").lower() == "y"

scan(host, ports, arguments, run_as_root)