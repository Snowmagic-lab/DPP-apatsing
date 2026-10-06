#!/usr/bin/env python3

table = 0
while table <= 10:
    multiplier = 0
    print(f"Table de {table}:", end="")

    while multiplier <= 10:
        print(f" {table * multiplier}", end="")
        multiplier += 1

    print()  # จบหนึ่งแม่แล้วค่อยขึ้นบรรทัดใหม่
    table += 1