# Network Monitor Tool

This Network Monitor Tool is a Python script designed to monitor changes in the network configuration of a Windows machine, including IP addresses, the default gateway, and the ARP table. It provides real-time updates on any changes detected in these areas, making it useful for network diagnostics and security monitoring.

## Features

- **IP Address Monitoring**: Detects changes in IP addresses assigned to network interfaces.
- **Default Gateway Monitoring**: Tracks changes in the default gateway configuration.
- **ARP Table Monitoring**: Observes modifications in the ARP (Address Resolution Protocol) table entries.

## Requirements

- Python 3.x
- [`psutil`](command:_github.copilot.openSymbolFromReferences?%5B%7B%22%24mid%22%3A1%2C%22path%22%3A%22%2Fhome%2Fguyacamole%2F.vscode%2Fextensions%2Fms-python.vscode-pylance-2024.6.1%2Fdist%2Ftypeshed-fallback%2Fstubs%2Fpsutil%2Fpsutil%2F__init__.pyi%22%2C%22scheme%22%3A%22file%22%7D%2C%7B%22line%22%3A0%2C%22character%22%3A0%7D%5D "../../../.vscode/extensions/ms-python.vscode-pylance-2024.6.1/dist/typeshed-fallback/stubs/psutil/psutil/__init__.pyi") library

## Installation

Before running the script, ensure you have Python installed on your Windows machine. You can download Python from [python.org](https://www.python.org/downloads/).

After installing Python, you need to install the [`psutil`](command:_github.copilot.openSymbolFromReferences?%5B%7B%22%24mid%22%3A1%2C%22path%22%3A%22%2Fhome%2Fguyacamole%2F.vscode%2Fextensions%2Fms-python.vscode-pylance-2024.6.1%2Fdist%2Ftypeshed-fallback%2Fstubs%2Fpsutil%2Fpsutil%2F__init__.pyi%22%2C%22scheme%22%3A%22file%22%7D%2C%7B%22line%22%3A0%2C%22character%22%3A0%7D%5D "../../../.vscode/extensions/ms-python.vscode-pylance-2024.6.1/dist/typeshed-fallback/stubs/psutil/psutil/__init__.pyi") library, which is used for retrieving information on network interfaces and addresses. Install [`psutil`](command:_github.copilot.openSymbolFromReferences?%5B%7B%22%24mid%22%3A1%2C%22path%22%3A%22%2Fhome%2Fguyacamole%2F.vscode%2Fextensions%2Fms-python.vscode-pylance-2024.6.1%2Fdist%2Ftypeshed-fallback%2Fstubs%2Fpsutil%2Fpsutil%2F__init__.pyi%22%2C%22scheme%22%3A%22file%22%7D%2C%7B%22line%22%3A0%2C%22character%22%3A0%7D%5D "../../../.vscode/extensions/ms-python.vscode-pylance-2024.6.1/dist/typeshed-fallback/stubs/psutil/psutil/__init__.pyi") using pip:

```shell
pip install psutil
```

## Running the Script

1. Open Command Prompt or PowerShell.
2. Navigate to the directory where you have saved the script.
3. Run the script using Python:

```shell
python main.py
```

## How It Works

Upon execution, the script performs the following actions:

1. **Initial Data Collection**: Gathers the current IP addresses, default gateway, and ARP table entries.
2. **Continuous Monitoring**: Every 10 seconds, the script checks for any changes in the IP addresses, default gateway, or ARP table entries compared to the initial data collected.
3. **Change Detection and Notification**: If any changes are detected in the network configuration, the script prints the old and new values to the console, providing real-time updates on the network state.

## Note

This script is designed to run on Windows due to its reliance on Windows-specific commands (`ipconfig` and `arp -a`). For running on other operating systems, modifications to the system command calls would be necessary.
