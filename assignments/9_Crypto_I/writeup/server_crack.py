#!/usr/bin/env python3

import hashlib
import string
import socket
import time

def serve(s):
    passwords = open("password.txt", 'r')
    character = string.ascii_lowercase
    data = s.recv(1024)
    print(data.decode())
    for p in passwords:
        for c in character:
            p = p.strip()
            hsh = hashlib.sha256(c.encode() + p.encode()).hexdigest()
            val = data.decode().split()
            x = len(val)
            if hsh == val[x - 2]:
                time.sleep(2)
                s.send(c.encode() + p.encode() + "\n".encode())
                return
def server_crack():
    server_ip = '134.209.128.58'
    server_port = 1337
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((server_ip, server_port))

    i = 0
    while i < 3:
        serve(s)
        i += 1
    print(s.recv(1024).decode())
if __name__ == "__main__":
    server_crack()
