import os
ip_Addr=[]
##
##  You will need to write the part that opens the file and stores it into the list name ip_Addr
##
filepath = "ipaddress.txt"
with open(filepath, 'r') as file:
    for line in file:
        ip_Addr.append(line.strip())
for ipaddr in ip_Addr:
    command = f"nmap -sC -sV {ipaddr}-oN {ipaddr}.txt --unprivileged"
    os.system(command)
