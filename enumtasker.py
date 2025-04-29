#!/usr/bin/python3


import os
import subprocess

targets_file = input("inserisi lal lista: ")
print("sto facendo la cartella")
loot_dir = "loot"
if not os.path.exists(loot_dir):
    os.makedirs(loot_dir)

print("ho fatto la cartella")
print("pingsweepin")
subprocess.run(f"nmap -sn -iL {targets_file} -oG pinged.txt", shell=True)

ips = set()
with open("pinged.txt","r") as f:
    for line in f:
        if "Up" in line:
            parts = line.split()
            if len(parts) >= 2:
                ips.add(parts[1])
#estrarrre
with open("ips.txt","w") as f:
     for ip in sorted(ips):
        f.write(ip + "\n")

# Servizi da enumerare con porte associate NO BRUTE dopo migliorare le porte perchè ne hanno di più.
services = {
    "ftp": "21",
    "ssh": "22",
    "telnet": "23",
    "smtp": "25",
    "pop3": "110",
    "rpc": "111",
    "netbios": "139",
    "smb": "445",
    "snmp": "161",
    "ldap": "389",
    "nfs": "2049",
    "mysql": "3306",
    "mssql": "1433",
    "rdp": "3389"
}
#ciclo sul dizionario lancia il comando per ognuno
for name, port in services.items():
    print(f"enumerando {name.upper()}...")
    output_file = os.path.join(loot_dir, f"{name}.txt")
    cmd = f"nmap -sV -p {port} --script 'not brute' -iL ips.txt -oN {output_file}"
    subprocess.run(cmd, shell=True)

print("enumerazione completata.")
