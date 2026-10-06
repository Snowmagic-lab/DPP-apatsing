#!/usr/bin/env python3
Num = input("Give me a number",)

if "." in str(Num):
    if ".00" in str(Num):
        print("This number is an integer.")
    else:
        print("This number is a decimal.")
else:
    print("This number is an integer.")