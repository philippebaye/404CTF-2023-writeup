import sympy as sp


# ---------------------------------------------------------------------------------------
# Découpage du message chiffré en blocs de 5 caractères, représenté sous forme de vecteur
# ---------------------------------------------------------------------------------------
'''
Les caracères sont encodés suivant leur code ascii, en commençant à 0
- a -> 0
- b -> 1
- ...
- y -> 24
- z n'est pas utilisé (on est en base 25)
'''
def decouper_message_en_bloc(message:str) -> []:
    taille_bloc = 5
    return [message[i:i+taille_bloc] for i in range(0, len(message), taille_bloc)]

def encoder_bloc_en_vecteur(bloc:str) -> []:
    zero = ord('a')
    return sp.Matrix(5, 1, [ord(c)-zero for c in bloc])

def decoder_vecteur_en_bloc(vecteur:[]) -> str:
    zero = ord('a')
    return ''.join([chr(code[0]+zero) for code in vecteur])

# -----------------------------------------------
# Matrices de chiffrement / déchiffrement de Hill
# -----------------------------------------------
matrice_chiffrement = sp.Matrix([[ 9,  4, 18, 20,  8],
                                 [11,  0,  2,  1,  3],
                                 [ 5,  6,  7, 10, 12],
                                 [13, 14, 15, 16, 17],
                                 [19, 21, 22, 23, 24]])
##print(f'{matrice_chiffrement = }')

matrice_dechiffrement = matrice_chiffrement.inv_mod(25)
##print(f'{matrice_dechiffrement = }')


# --------------------------------------
# Déchiffrement du message bloc par bloc
# --------------------------------------
# Le message à déchiffrer
message_chiffre = 'ueomaspblbppadgidtfn'
print(f'{message_chiffre = }')

# Le message déchiffré
message_en_clair = ''
for bloc_message_chiffre in decouper_message_en_bloc(message_chiffre):
    vecteur_chiffre = encoder_bloc_en_vecteur(bloc_message_chiffre)
    vecteur_enclair = (matrice_dechiffrement * vecteur_chiffre % 25).tolist()
    bloc_message_enclair = decoder_vecteur_en_bloc(vecteur_enclair)
    #print(bloc_message_enclair, end='')
    message_en_clair += bloc_message_enclair

print(f'{message_en_clair = }')
