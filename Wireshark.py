################################## WIRESHARK ##################################

#   ● Traffic Capture and traffic filtering with wreshark

#   ● Man in The Middle with Wireshark

#   ● WLAN traffic Man in The Middle with Wireshark


# =============================================================================

# WIRESHARK


#   ● Packet analyser / traffic sniffer

#   ● Open-source

#   ● Cross-platform

#   ● Fancy GUI

#   ● https://www.wireshark.org


# =============================================================================

# Data Packets Capturing


# To start capturing

#   ● Select a network interface

#   ● Click on the blue shark fin button / press Ctrl + E


# To stop capturing

#   ● Click on the red stop button / press Ctrl + E


# Top Frame:

# Number | Time | Source | Destination | Protocol | Length | Info


# Middle frame example :

#   ► Frame

#   ► Linux cooked capture

#   ► Internet Protocol version, source, destination

#   ► Transmission control protocol, src port, dst port, seq, len

# Buttom Frame:

# Data


# =============================================================================

# WIRESHARK FILTERS

# There are 2 ways to filter:

#   ● Build a filter via the fancy GUI (Expression button)

#   ● Type of filter into the "Apply a display filter" entry field (below the toolbar)

#   ● https://wiki.wireshark.org/DisplayFilters



# MOST COMMON WIRESHARK FILTERS

#   tcp.port eq 80

#   tcp.srcport==80

# Filter for http and https traffic:

#   tcp.port==443 or tcp.port==80

#   ssl or http

#   tcp.port in {80 443 8080}

#   tcp.port == 80 || tcp.port == 443 || tcp.port == 8080


# Filter for a protocol:

# tcp

# udp

# dns


# IP address:

# ip.addr == 192.168.1.1

# (ip.addr == 192.168.1.1)


# Example for Web Traffic:

# http.request.url == https://demo.testfire.net

# http.host matches "acme\[org|com|net]

# http.response.code == 200

# http.request.method == "GET"

# tcp contains "admin"




#  =============================================================================


# MITM :-

# start with > ping Target_IP

#   ● 






































