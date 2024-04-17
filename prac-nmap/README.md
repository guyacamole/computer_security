# Network Scanner

This is a simple network scanner built with Python and the nmap library. It allows you to scan a host for open ports and other information.

## Installation

1. Clone this repository.
2. Navigate to 'prac-nmap' of the cloned repository's directory.
3. Create a virtual environment named `.venv`:

```bash
python3 -m venv .venv
```

4. Activate the virtual environment:

On Linux or MacOS:

```bash
source .venv/bin/activate
```

On Windows:

```cmd
.venv\Scripts\activate
```

5. Install the required Python packages using pip:

```bash
pip install -r requirements.txt
```

## Usage

Run the `main.py` script:

```bash
python3 main.py
```

When prompted, enter the following information:

- The host you want to scan.
- The ports you want to scan (comma-separated).
- Any additional arguments for the nmap command.
- Whether you want to run the scan as root (y/n).

The script will then perform the scan and print out the results.

## Note

This script uses the nmap command, which may require root privileges depending on your system configuration and the options you choose. If you choose to run the scan as root, you will be prompted for your password.

