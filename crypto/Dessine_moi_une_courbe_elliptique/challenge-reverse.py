import math
import hashlib
from Crypto.Cipher import AES


# ------------------------
# Données extraites du fichier data.txt
# ------------------------
# Coordonnées des 2 points G et H qui sont sur la Courbe Elliptique construite GF(p)
x1, y1 = 93808707311515764328749048019429156823177018815962831703088729905542530725, 144188081159786866301184058966215079553216226588404139826447829786378964579
x2, y2 = 139273587750511132949199077353388298279458715287916158719683257616077625421, 30737261732951428402751520492138972590770609126561688808936331585804316784
# modulo
p = 231933770389389338159753408142515592951889415487365399671635245679612352781
# le flag chiffré
hexdump_of_encrypted_flag = '8233d04a29befd2efb932b4dbac8d41869e13ecba7e5f13d48128ddd74ea0c7085b4ff402326870313e2f1dfbc9de3f96225ffbe58a87e687665b7d45a41ac22'
hexdump_of_iv = '00b7822a196b00795078b69fcd91280d'


# ------------------------------------------------------------
# Calcul des coefs 'a' et 'b' de la courbe elliptique utilisée
# ------------------------------------------------------------
# la courbe est de la forme : y**2 = x**3 + a.x + b  (modulo p)

# Calcul de a, comme on a 2 points : [(y1**2−y2**2)−(x1**3−x2**3)]⋅= a.(x1−x2)  (modulo p)

# Vérification que (x1-x2) a un inverse modulaire (avec p comme modulo)
g = math.gcd(x1-x2, p)
if g != 1:
    print('(x1-x2) et p ne sont pas premiers entre eux --> snif')
    quit()

# Comme on a un inverse modulaire : a = [(y1**2−y2**2)−(x1**3−x2**3)] . (x1−x2)**-1  (modulo p)
a = ( (pow(y1,2,p)-pow(y2,2,p)) - (pow(x1,3,p)-pow(x2,3,p)) ) * pow(x1-x2, -1, p)
a %= p
print(f'{a = }')

# Comme : y**2 = x**3 + a.x + b 
# Donc : b = y**2 - x**3 - a.x (modulo p)
b = pow(y1,2,p) - pow(x1,3,p) - a*x1
b %= p
print(f'{b = }')


# -------------
# Déchiffrement
# -------------
key = str(a) + str(b)
print(f'{key = }')

iv = bytes.fromhex(hexdump_of_iv)
aes = AES.new(hashlib.sha1(key.encode()).digest()[:16], AES.MODE_CBC, iv=iv)

encrypted_flag = bytes.fromhex(hexdump_of_encrypted_flag)
flag = aes.decrypt(encrypted_flag)
print(f'{flag = }')
