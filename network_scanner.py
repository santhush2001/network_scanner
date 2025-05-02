import nmap

scanner = nmap.PortScanner()

target = input("Enter IP address or range (e.g., 192.168.1.0/24): ")
print(f"Scanning {target}...")
scanner.scan(hosts=target, arguments='-sn')  # Use -sn instead of deprecated -sP

for host in scanner.all_hosts():
    print(f"Host: {host} ({scanner[host].hostname()})")
    print(f"  State: {scanner[host].state()}")
