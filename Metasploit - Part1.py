##############################  METASPLOIT ##############################



# step 1 : Installing Metasploit on Linux       --(Debian / Ubuntu)
# cmd >>>  apt install metasploit-framework     --(package)

# On CentOS / Redhat you can the yum utility to do the same:
# cmd >>>  yum install metasploit-framework


# step 2 : Find out the version of Metasploit and updating
# cmd >>>  sudo msfconsole

# Update command :
# msf6 > apt msfupdate / apt update / apt install metasploit-framework



# ==============================================================================

# Basics of Penetration testing (VAPT):

#   ● Information Gathering / Reconnaissance  - (IP, PORTS, PROTOCOLS, VERSION)

#   ● Vulnerability Analysis  - which type of version available on system to exploit vulnerability

#   ● Exploitation  - check if version exploit or not like bugs or identify vulnerability.

#   ● Post Exploitation  - if once exploit then enter an get shell ssh, run more commands, details etc.

#   ● Report  - write report in company.



# ==============================================================================

# Basic of Metasploit Framework is divided by module wise.

# Modules of Metasploit Framework
# → The core functionalities that Metasploit provided can be summarized by some
#   of the modules :

# 1). Exploits  - It's program that attack the vulnerability of the target.

# 2). Payloads  - perform task after exploit like reverse shell, bind shell,
#                 meterspeter, establish connectivity to the attacking machine.

# 3). Auxiliaries - It's programs that do not directly exploit a system. These
#                   help you scan the victim machine for info gathering purpose.

# 4). Encoders  - encrypt the code for anti-virus has many signatures of them
#                 already in their databases. So, encoder will not guarantee anti-virus evasion.



# ==============================================================================

# Components of Metasploit Framework

# Metasploit is open-source and it is written in Ruby.

# There are some key components :

#   ● msfconsole - cli or gui that is used by the metasploit framework.

#   ● msfdb - store and organize your scan results in the database to access it use PostgreSQL DB.

#   ● msfvenom - It's tool for create your own payloads (venoms to inject in your victim machine).

#   ● meterpreter - It is advanced payload that has lot of functionalities built into it.
#                   meterpreter quite difficult to trace & locate once in the sys.
#                   It can capture screenshot, dump passwd hashes, many more.




# ==============================================================================


# Metasploit location on the drive

# Note - 1st exit from anywhere & come on the root dir)

#   ● > cd /usr/share/metasploit-framework

#   ● > ls

#   ● > cd modules

#   ● > cd linux / windows

#   ● > cat file_name.rb



# ==============================================================================


# Basic commands of Metasploit Framework

#   ● > msfconsole (Fire up the Metasploit console by typing in)

#   ● > show -h (how command will show you specific modules or all the modules)

#   ● > search

#   ● > use (you can select the module by the use cmd followed by the name or id of mod.) 

#   ● > info (you could get the desc by looking at the original code of the mod.)

#   ● > options / show options

#   ● > set (set a value to a variable)

#   ● > show payloads (you will get the only payloads that are compatible with the exploit)

#   ● > Check (Check if the exploit will work or not).


# ==============================================================================




