from os import urandom
import base64
from time import sleep

with open("shaks12.txt", "r") as f:
    shakespeare = f.read()
n = 0
while True:
    n += 1
    random = base64.b64encode(urandom(len(shakespeare))).decode("utf-8")[:len(shakespeare)]
    print(f"{random}\n\n")
    print(f"{n} attempts\n")
    if random == shakespeare:
        print(f"A monkey typed the complete works of shakespeare somehow after {n} attempts")
        break
    sleep(0.1)

