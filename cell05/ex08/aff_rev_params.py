#!/usr/bin/env python3
import sys
i = 1
k = len(sys.argv) - 1

if len(sys.argv) != 1:
     while i != len(sys.argv):
         print(sys.argv[k])
         k = k-1
         i = i+1
        
     
         
else:
    print("none")