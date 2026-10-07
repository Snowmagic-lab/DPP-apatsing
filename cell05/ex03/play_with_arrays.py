#!/usr/bin/env python3

num = [2, 8, 9, 48, 8, 22, -12, 2]
Newnum = []

for number in num:
    if number > 5:
       Newnum.append(number + 2)

print("Original array:", set(num))
print("New array", set(Newnum))