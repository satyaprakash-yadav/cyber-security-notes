#       ---------------------------------- OSI MODEL ----------------------------------
 
#                            ________________
#                     __    |                |
#                    |      | Application    | --------► App / Application / WebApp
#                    |      |________________|        
#     Software/   ___|      |                |
#     Application    |      | Presentation   | --------► .png / .docx / .xml / .html / .txt / .mkv / .mp3 
#     Layer          |      |________________|
#                    |      |                |
#                    |__    | Session        | --------► end to end connection until data receive
#                           |________________|
#                           |                |
#                           | Transport      | --------► Fragmentation
#                           |________________|
#                    __     |                |
#                   |       | Network        | --------► adds / to --> from  / IP / MAC / Router
#                   |       |________________|
#                   |       |                |
#     Hardware   ___|       | Data Link      | --------► To - Encryption / from - Decryption 
#     Layer         |       |________________|
#                   |       |                |
#                   |       | Physical       | --------► via optical fibre / wireless or bit / analog
#                   |__     |________________|
#                           




# Consider , 400 pages of file send to the one company to the another company then how it to be transfer the file.
# lets see , practical example :- 
   

#                                  SENDER                                    RECEIVER
#                             ________________                           ________________
#                        __  |                |                         |                |
#                       |    | Application    | --------► 400 pages     | Application    | 
#                       |    |________________|               |         |________________| 
#        Software /  ___|    |                |               ↓         |                |
#        Application    |    | Presentation   | --------►   check       | Presentation   |
#        Layer          |    |________________|           .extension    |________________|
#                       |    |                |               ↓         |                |
#                       |__  | Session        | --------► check(conn)   | Session        |
#                            |________________|           Availability  |________________|
#                            |                |               ↓         |                |
#                            | Transport      | --------► fragement     | Transport      |
#                            |________________|           packets | | | |________________|
#                        __  |                |               ↓         |                |
#                       |    | Network        | --------► To ---> From  | Network        |
#                       |    |________________|           check adds/IP |________________|
#                       |    |                |               ↓         |                |
#        Hardware    ___|    | Data link      | --------► encrypte /    | Data link      |
#        Layer          |    |________________|           decrypte      |________________|
#                       |    |                |               ↓         |                |
#                       |    | Physical       | --------► wireless | bit| Physical       |
#                       |__  |________________|          /analog/opt fib|________________|
#                                    |                                          ↑     
#                                    |__________________________________________|
#                                      If every thinks are perfectly then files           
#                                       are transfer to the receiver.  


