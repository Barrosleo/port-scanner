import socket
from datetime import datetime

# Port Scanning Function
def scan_ports(ip):
    print(f"Scanning ports on {ip}")
    start_time = datetime.now()
    
    open_ports = []
    for port in range(1, 1025):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)
        result = sock.connect_ex((ip, port))
        if result == 0:
            open_ports.append(port)
        sock.close()
    
    end_time = datetime.now()
    total_time = end_time - start_time
    
    print(f"Open ports: {open_ports}")
    print(f"Time taken: {total_time}")

if __name__ == "__main__":
    target_ip = input("Enter the IP address to scan: ")
    scan_ports(target_ip)
