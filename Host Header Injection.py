#                   ------------------------------------------- HOST HEADER INJECTION -------------------------------------------


#                                                                       http header             ___
# BurpSuit                                                       ______   request    ______    | - | 
#                                                               |      | ---------> |      |   | - | 
#       Http header                                             |______| <--------- |______|   | - | 
#           |__ Connection                                         /\     response     /\      |_-_| 
#           |                                                    Client                       Server    
#           |__ Content-encoding                                        http header            |
#           |                                                           ----|-|----            | 
#           |__ Content-length                                                                 | 
#           |                                                                                __↓_ 
#           |__ Transfer-encoding                                                           |_CA_| Proxy
#           


#       Request http header
#           |__ Accept header   :-
#           |
#           |__ Accept encoding :- |-------| |-------|
#           |
#           |__ Authorization   :-
#           |
#           |__ Cookie          :-
#           |
#           |__ host            :- IP / domain / url
#               
#               origin   _________
#               referer  _________
#               ____________      __________
#              | user-agent |    |---       |        
#              |____________|    |---_______|



#       Response http header      ____
#           |__ Cache control :- |____| - [cache server]
#           |
#           |__ Etag          :- 
#           |
#           |__ Expires       :-
#           |
#           |__ location      :-
#           |
#           |__ Server        :-
#           |    
#           |__ Set cookie    :-    
#           |    
#           |__ Authenticate  :-  IIS
#           |
#           |__ X-Frame options :-



#           Ipv4                                                     Class of IP
#           32 - bits logical adds                                  Class A ---> 1 - 126   
#           4 octet                                                 Class B ---> 128 - 191
#           0-255                                                   Class C ---> 192 - 223   ___
#                                                                   Class D ---> 224            |___ Research center
#           IP ---> Network ID + Host ID                            Class E ---> 240 or more ___|
#                                                               
#                                                                   ping :- 127.0.0.1
#           Replay ----> loop back
#
#



#       MAC (48 - bits) Hexadecimal                                                 address
#                                                                                      /\
#       Physical adds (PC)                                                            /  \
#       Hardware adds                                                                /    \
#       BIA (Burnt-in-add)                                                    logical(IP) Physical(MA)      
#                                   (Cisco)
#                                   48 bits
#                   ___________________|___________________             IPConfig / all
#                  |                                       | 
#              ____↓____                               ____↓____  
#             | 24 bits |                             | 24 bits |  
#             |___OUI___|                             |_vendorb_|
#
#       IANA (Internet Addressing Number As)
#
#
#
#

