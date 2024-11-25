# Project: Network Port Scanner

## Project Description
The Network Port Scanner is a Python-based tool designed to identify open ports within a network. Open ports are crucial for communication between devices, but they can also pose a security risk if left unmonitored. This tool helps administrators and penetration testers quickly and efficiently check for open ports on one or multiple hosts.

## Features
- Single Host Scanning: Scan a single IP address for open ports within a specified range.
- Multi-Host Scanning: Scan multiple IP addresses sequentially for open ports.
- Fast and Efficient: Uses threading to speed up the scanning process.
- Real-Time Results: Displays open ports in real-time during the scan.
- Lightweight and Fast: Designed for simplicity and performance.
- Error Handling: Handles unreachable hosts and invalid input gracefully.

## Technologies Used

### Programming Language: Python
### Libraries:
- socket: for network communication
- sys: For handling command-line arguments.
- datetime: To calculate scan duration.
