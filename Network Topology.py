#     ------------------------------------------ Network Topology -------------------------------------

# Network Topology :-
# 1). The arrangement of network that comprises nodes and connecting lines between sender and receiver is called Network Topology.
# 2). The way of design to connect devices to communicate is called network topology.


# Types of Network Topology :-

# 1). Star Topology 
# 2). Bus  Topology
# 3). Ring Topology
# 4). Tree Topology
# 5). Mesh Topology
# 6). Hybrid Topology


# 1). Star Topology  :- All devices are connected to the single hub and hub is the central node and all other nodes are connected to the central node.
# It is Robust. If one link fails only that link will affect and not other than that and also cost of installation is high and easy to Troubleshoot.

#            Node 3
#              ↑ 
#              | 
#              | 
# Node 1 ---- HUB ---- Node 2
#              | 
#              | 
#              ↓     
#            Node 4


# 2). Bus Topology :- It is a Network type in which every computer and network device is connected to a single cable and it is bi-directional.
# It is a multi-point connection and a non-robust topology because if the backbone fails the topology crashes.
# Coaxial or twisted pair cables are mainly used in bus-based networks that support up to 10 Mbps and less secure.

#             Node 1                      Node 3
#               ↑                           ↑
#               |                           |
#               |    backbone coaxial cable |
# ||____________|___________________________|_________________________________||
# ||                         |                              |                 ||
# Terminator                 | droplines                    |
#                            |                              |
#                            ↓                              ↓
#                          Node 2                         Node 4


# 3). Ring Topology :- It forms a ring connecting devices with exactly two neighboring devices and MSAU(Multi Station Access unit).
# Suppose there are 50 nodes someone wants to send data to the last node 50 then data have pass through 49 nodes to reach out node 50th and also.
# Token passing: It is a network access method in which a token is passed from one node to another node.
# Token: It is a frame that circulates around the network and Less secure and Troubleshooting is difficult.

#                 Station 1
#                     ↑  
#       _____________||____________    || - Terminators/Repeaters
#      |             ||            |  
#      |                           |                                  
# Station 2                        || → Station 3
#      |                           | 
#      |_____________||____________|  
#                    ||
#                     ↓ dropline  
#                 Station 4


# 4). Tree Topology :- It is hierarchical flow of data.
# We can add new devices to the existing network and it becomes difficult to reconfigure.
# Error detection and error correction are very easy in a tree topology.

#     system 1 ◄---------central---------► system 2
#                         hub 
#                       /     \
#                      /       \
#                     ↙         ↘
#            Secondary hub     Secondary hub       
#             /    |     \                /|\  
#            /     |      \              / | \ 
#           ↙      ↓       ↘            ↙  ↓   ↘
#   system 3    system 4  system 5    sys 6 sys 7 sys 8


# 5). Mesh Topology :- Every device is connected to another device via a particular channel.
# The fault is diagnosed easily. Data is reliable because data is transferred among the devices through dedicated channels or links.
# It is robust and also Provides security and privacy.
# Installation and configuration are difficult.
# The cost of cables is high as bulk wiring is required, hence suitable for less number of devices.
# The cost of maintenance is high.


# 6). Hybrid Topology :-  It is combination of various types of topology like star , bus , tree , etc.
# This topology is very flexible and the size of the network can be easily expanded by adding new devices.
# The infrastructure cost is very high as a hybrid network requires a lot of cabling and network devices.









