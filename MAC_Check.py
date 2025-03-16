import os
import subprocess
import re
import datetime

trusted_mac_table = "/opt/network_monitor/trusted_macs.txt"
log_dir = "/opt/network_monitor/logs"
log_file = "/opt/network_monitor/logs/network_log.txt"

if not os.path.exists(trusted_mac_table):
    print("List not found. Please create a trusted MAC address table.")
    exit()

subprocess.run(["ping", "-c", "1", "192.168.1.255"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
output = subprocess.run(["arp", "-a"], capture_output=True, text=True)
mac_addresses = re.findall(r"([0-9a-fA-F]{2}:[0-9a-fA-F]{2}:[0-9a-fA-F]{2}:[0-9a-fA-F]{2}:[0-9a-fA-F]{2}:[0-9a-fA-F]{2})", output.stdout)

for mac in mac_addresses:
    print(mac)

with open(trusted_mac_table, "r") as trusted_mac_f:
    trusted_macs = [line.strip() for line in trusted_mac_f if line.strip()]

unknown_macs = []
for mac in mac_addresses:
    if mac not in trusted_macs:
        unknown_macs.append(mac)

if unknown_macs:
    print("\n Unkown MAC address found:")
    for mac in unknown_macs:
        print(mac)
    with open(log_file, "a") as log:
        timestamp = timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log.write(f"\n[{timestamp}] Unknown MAC Addresses Detected:\n")
        for mac in unknown_macs:
            log.write(f"{mac}\n")

else:
    print("\nNo unknown MAC found.")

if not os.path.exists(log_dir):
    os.makedirs(log_dir)

