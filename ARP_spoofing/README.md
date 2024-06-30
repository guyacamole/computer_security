
# ARP Spoofing and Packet Sniffing Script

This script is designed to perform ARP spoofing and packet sniffing on a local network. It requires root privileges to run and utilizes the Scapy library for network manipulation and packet analysis.

## Prerequisites

- Python 3.x
- Scapy
- Root privileges

## Installation

1. Clone this repository or download the script.
2. Ensure Python 3.x is installed on your system.
3. Install Scapy using pip:

```bash
pip install scapy
```

4. Create a virtual environment (optional):

```bash
python -m venv .venv
```

5. Activate the virtual environment:

- On Linux/Mac:

```bash
source .venv/bin/activate
```

- On Windows:

```cmd
.venv\Scripts\activate
```

## Running the Script

To run the script, you must have root privileges. Use the following command:

```bash
sudo .venv/bin/python main.py
```

## Expected Output

Upon successful execution, the script will start sniffing packets on the network and display them in the terminal. Example output:

```
Packet: Ether / IP / TCP 192.168.0.17:40344 > 192.168.0.2:2869 S
Packet: Ether / IP / TCP 192.168.0.17:40344 > 192.168.0.2:2869 A
...
Packet: Ether / IP / TCP 192.168.0.17:35046 > 192.168.0.2:2869 A
```

This output indicates that the script is capturing TCP packets being sent to and from the target IP address specified in the script.

## Stopping the Script

To stop the script, simply press `Ctrl+C` in the terminal. This will safely terminate the ARP spoofing and packet sniffing processes.