import socket

print("=" * 50)
print("PORT SCANNER")
print("=" * 50)

target = input("Enter target IP or hostname: ")

print(f"\nScanning {target}...\n")

for port in range(1, 1025):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(0.5)

    result = sock.connect_ex((target, port))

    if result == 0:
        print(f"Port {port} is OPEN")

    sock.close()

print("\nScan Complete.")
