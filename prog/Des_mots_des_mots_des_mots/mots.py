'''
$ nc challenges.404ctf.fr 30980
Commençons. Je te propose de démarrer en transformant mon nom.
Tout d'abord retourne mon nom sans modifications.
Règle 0 : Aucune modification
Entrée : {cosette}
>> cosette
Je vois que tu as compris. La première règle de ce langage est très simple.
Règle 1 : Inverser les lettres
Entrée : {cosette}
>> ettesoc
Oui c'est bien. Maintenant la deuxième règle est un peu plus difficile.
Règle 2 :
- Si le mot à un nombre de lettres pair, échanger la 1ere et la 2e partie du mot obtenu
- Sinon, enlever toutes les lettres du mot correspondant à la lettre centrale
Entrée : {cosette}
>> ttsoc
Tu t'en sors très bien ! Continuons avec la troisième règle.
Règle 3 :
_Si le mot a 3 lettres ou plus_ :

- Si la 3e lettre du mot obtenu est une consonne, "décaler" les voyelles vers la gauche dans le mot original, puis réappliquer les règles 1 et 2.
- Sinon : la même chose mais les décaler vers la droite.

> Ex de décalage : _poteau => petauo_ // _drapeau => drupaea_
Entrée : {cosette}
>> ottsc
Nous avons presque fini, la quatrième règle est la plus complexe.
Règle 4 :
- Pour `n` allant de 0 à la fin du mot, si le caractère `c` à la position `n` du mot est une consonne (majuscule ou minuscule), insérer en position `n+1` le caractère de code ASCII `a = ((vp + s) % 95) + 32`, où `vp` est le code ASCII de la voyelle précédant la consonne `c` dans l'alphabet (si `c = 'F'`, `vp = 'E'`), et `s = SOMME{i=n-1 -> 0}(a{i}*2^(n-i)*Id(l{i} est une voyelle))`, où `a{i}` est le code ASCII de la `i`-ième lettre du mot, `Id(x)` vaut `1` si `x` est vrai, `0` sinon, et `l{i}` la `i`-ième lettre du mot. _Attention à bien appliquer cette règle aussi sur les caractères insérés au mot._

> Ex : _futur => f&ut\\ur@_

- Enfin, trier le mot par ordre décroissant d'occurrences des caractères, puis par ordre croissant en code ASCII pour les égalités

> Ex de tri : _patate => aattep_
Entrée : {cosette}
>> PPtt!15QRUWcos
Bravo ! Maintenant je vais te donner un chapitre dont j'ai besoin de la traduction complète.
Chaque mot est écrit en minuscule sans accents ni caractères spéciaux et sont séparés par un espace. Tu as 5 secondes pour répondre.
Entrée : {palais episcopal digne etait attenant hopital palais episcopal etait vaste hotel pierre commencement siecle dernier monseigneur henri puget docteur theologie faculte paris simore lequel etait eveque digne palais etait logis seigneurial avait grand appartements eveque salons antichambres honneur large promenoirs arcades selon ancienne florentine jardins plantes magnifiques arbres salle manger longue superbe galerie etait chaussee ouvrait jardins monseigneur henri puget avait donne manger ceremonie juillet messeigneurs charles brulart genlis archeveque prince embrun antoine mesgrigny capucin eveque grasse philippe vendome grand prieur france saint honore lerins francois berton grillon eveque baron vence cesar sabran forcalquier eveque seigneur glandeve soanen pretre oratoire}
>> 
'''

def regle1(mot:str) -> str:
    return mot[::-1]

def regle2(mot:str) -> str:
    '''
    - Si le mot à un nombre de lettres pair, échanger la 1ere et la 2e partie du mot obtenu
    - Sinon, enlever toutes les lettres du mot correspondant à la lettre centrale
    '''
    longueur_mot = len(mot)
    if longueur_mot & 0x1:
        # longueur impaire -> on supprime toutes les occurrences de la lettre centrale
        indice_lettre_centrale = longueur_mot//2
        lettre_centrale = mot[indice_lettre_centrale]
        return ''.join(c for c in mot if c != lettre_centrale)
    else:
        # longueur paire -> on échange les 2 parties du mot
        milieu_mot = longueur_mot//2
        return ''.join(mot[milieu_mot:] + mot[:milieu_mot])

voyelles = 'aeiouyAEIOUY'
def regle3(mot_original:str, mot:str) -> str:
    '''
    _Si le mot a 3 lettres ou plus_ :
        - Si la 3e lettre du mot obtenu est une consonne, "décaler" les voyelles vers la gauche dans le mot original, puis réappliquer les règles 1 et 2.
        - Sinon : la même chose mais les décaler vers la droite.
    '''
    longueur_mot = len(mot)
    if longueur_mot > 2:
        # mot d'au moins 3 lettres
        mot_voyelles_decalees = [c for c in mot_original]
        index_voyelles_mot_original = [idx for idx,c in enumerate(mot_original) if c in voyelles]
        lettre_3 = mot[2]
        if lettre_3 in voyelles:
            # décalage des voyelles vers la droite
            index_voyelles_mot_voyelles_decalees = index_voyelles_mot_original[1:] + index_voyelles_mot_original[:1]
        else:
            # décalage des voyelles vers la gauche
            index_voyelles_mot_voyelles_decalees = index_voyelles_mot_original[-1:] + index_voyelles_mot_original[:-1]

        for ancien_index, nouvel_index in zip(index_voyelles_mot_original, index_voyelles_mot_voyelles_decalees):
            mot_voyelles_decalees[nouvel_index] = mot_original[ancien_index]
        ##print(mot_voyelles_decalees)

        return regle2(regle1(mot_voyelles_decalees))
    else:
        return mot

consonnes = 'bcdfghjklmnpqrstvwxzBCDFGHJKLMNPQRSTVWXZ'
voyelle_precedent_consonne = {
       'b': 'a', 'c': 'a', 'd': 'a',
       'f': 'e', 'g': 'e', 'h': 'e',
       'j': 'i', 'k': 'i', 'l': 'i', 'm': 'i', 'n': 'i',
       'p': 'o', 'q': 'o', 'r': 'o', 's': 'o', 't': 'o',
       'v': 'u', 'w': 'u', 'x': 'u',
       'z': 'y',
       'B': 'A', 'C': 'A', 'D': 'A',
       'F': 'E', 'G': 'E', 'H': 'E',
       'J': 'I', 'K': 'I', 'L': 'I', 'M': 'I', 'N': 'I',
       'P': 'O', 'Q': 'O', 'R': 'O', 'S': 'O', 'T': 'O',
       'V': 'U', 'W': 'U', 'X': 'U',
       'Z': 'Y'}

import collections

def regle4(mot:str) -> str:
    '''
    - Pour `n` allant de 0 à la fin du mot,
        si le caractère `c` à la position `n` du mot est une consonne (majuscule ou minuscule),
          insérer en position `n+1` le caractère de code ASCII `a = ((vp + s) % 95) + 32`,
            où `vp` est le code ASCII de la voyelle précédant la consonne `c` dans l'alphabet (si `c = 'F'`, `vp = 'E'`),
            et `s = SOMME{i=n-1 -> 0}(a{i}*2^(n-i)*Id(l{i} est une voyelle))`,
              où `a{i}` est le code ASCII de la `i`-ième lettre du mot,
              `Id(x)` vaut `1` si `x` est vrai, `0` sinon,
              et `l{i}` la `i`-ième lettre du mot.
        _Attention à bien appliquer cette règle aussi sur les caractères insérés au mot._
    '''
    '''
    new_mot = mot
    numero_car = 0
    longueur_mot = len(new_mot)
    while numero_car < longueur_mot:
        #c = new_mot[numero_car]
        if new_mot[numero_car] in consonnes:
            vp = ord(voyelle_precedent_consonne[new_mot[numero_car]])
            s = 0
            for i in range(numero_car-1, -1, -1):
                if new_mot[i] in voyelles:
                    s += ord(new_mot[i]) << (numero_car-i)
            a = chr(((vp + s) % 95) + 32)
            ##print(new_mot[numero_car], a)
            new_mot = new_mot[:numero_car+1] + a + new_mot[numero_car+1:]
            ##print(new_mot)
            longueur_mot = len(new_mot)
        numero_car += 1   
    '''
    new_mot = mot
    n = 0
    longueur_mot = len(new_mot)
    while n < longueur_mot:
        c = new_mot[n]
        if c in consonnes:
            vp = ord(voyelle_precedent_consonne[c])
            s = 0
            for i in range(n-1, -1, -1):
                if new_mot[i] in voyelles:
                    s += ord(new_mot[i]) << (n-i)
            a = chr(((vp + s) % 95) + 32)
            ##print(c, a)
            new_mot = new_mot[:n+1] + a + new_mot[n+1:]
            ##print(new_mot)
            longueur_mot = len(new_mot)
        n += 1

    '''
    - Enfin, trier le mot par ordre décroissant d'occurrences des caractères, puis par ordre croissant en code ASCII pour les égalités
    '''
    comptage = collections.Counter(new_mot)
    comptage_trie = sorted(comptage.items(), key=lambda x: (-x[1], ord(x[0])))
    final_mot = ''
    for car, nb_car in comptage_trie:
        final_mot += car * nb_car
    ##print(f'{final_mot=}')
    return final_mot

# Test du tuto    
data_in = 'cosette'
print(f'r1= {regle1(data_in)}')
print(f'r2= {regle2(regle1(data_in))}')     
print(f'r3= {regle3(data_in, regle2(regle1(data_in)))}')
print(f'r4= {regle4(regle3(data_in, regle2(regle1(data_in))))}')

# Test regle 3
print(regle3("poteau", "poteau"), regle3("drapeau", "drapeau"))


# ----------------------------------
# Partie interactive avec le serveur
# ----------------------------------
from pwn import *

# Paramètres de connexion
HOST, PORT = "challenges.404ctf.fr", 30980

# Ouvre la connexion au serveur
io = remote(HOST, PORT)

# Tuto
mot_tuto = 'cosette'
io.sendlineafter(b'>> ', mot_tuto.encode())
io.sendlineafter(b'>> ', regle1(mot_tuto).encode())
io.sendlineafter(b'>> ', regle2(regle1(mot_tuto)).encode())
io.sendlineafter(b'>> ', regle3(mot_tuto, regle2(regle1(mot_tuto))).encode())
io.sendlineafter(b'>> ', regle4(regle3(mot_tuto, regle2(regle1(mot_tuto)))).encode())

# Récupération des données à traiter
input_data = io.recvuntil(b'>> ').decode().strip().split('{')[1].split('}')[0]
print(input_data)

# Traduction 
reponse = []
for data in input_data.split():
    reponse.append(regle4(regle3(data, regle2(regle1(data)))))
reponse = ' '.join(reponse)
print(reponse)

# Envoi de la réponse
io.sendline(reponse.encode())

# Récupération de la réponse (gagné ou pas)
final_message = io.recvall()
print(final_message.decode().strip())

# Fermeture de la connexion
io.close()
