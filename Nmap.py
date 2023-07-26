# ================================== NMAP ====================================

# Basic scanning technique

#   ● > Nmap Target_IP (Single IP Scan)

#   ● > Nmap Target_1 Target_2 (Scan Multiple Target)

#   ● > Nmap 192.168.1.1-100 (Scan a Range og IP)

#   ● > Nmap 192.168.1.0/24 (Scan Entire Subnet)

#   ● > cat list.txt

#   ● > Nmap 192.168.1.0/24

#   ● > Nmap 192.168.1.0/24 - exclude 192.168.1.100



# Discovery Options


#   ● > nmap -Pn 192.168.1.100 (Don't Ping)

#   ● > nmap -sP 192.168.1.0/24  (Ping only Scan)

#   ● > nmap -traceroute demo.testfire.net


# Advanced scanning options:

#   ● > nmap -sS 192.168.1.1 (TCP SYN Scan)

#   ● > nmap -sT 192.168.1.1 (TCP Connect Scan)

#   ● > nmap -sF 192.168.1.1 (TCP Fin Scan)

#   ● > nmap -sX 192.168.1.1 (Xmas Scan)



# Port Scanning options:

#   ● > nmap -F 192.168.1.1 (Fast Scan , only 100 Ports)

#   ● > nmap -p 80 192.168.1.1 (Scan Specific Ports)\



# Operating System & Service Detection

#   ● > nmap -O 192.168.1.1 (OS Detection)

#   ● > nmap -sV 192.168.1.1 (Service Version Detection)


# Timing Options

#   ● >  nmap -T4 192.168.1.1  T0(Extremely Slow), T5 Very Fast and Aggresive Scan


# Evading Firewall

#   ● > nmap -f 192.168.1.1 (Fragment probes into 8-bytes packets)

#   ● > nmap -D RND:10 192.168.1.1 (10 Random Decoy)



# Output Options


#   ● > nmap -oX scan.xml 192.168.1.1 (XML File)



# Nmap Scripting Engine (NSE)

#   ● > nmap --script [script.nse] Target_IP

#   ● > nmap --script default Target_IP
