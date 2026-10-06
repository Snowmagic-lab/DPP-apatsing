#!/usr/bin/env python3
x = 0
First = str(input("What you gotta say? : ", ))

Stop = "STOP"

while x == 0:
   User = str(input("I got that! Anything else? : ", ))
   if User in Stop:
      break