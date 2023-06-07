import re
import numpy as np

# Le message à déchiffrer
message_chiffre = 'ueomaspblbppadgidtfn'
print(f'{message_chiffre = }')

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
    return np.array([[ord(c)-zero] for c in bloc])

def decoder_vecteur_en_bloc(vecteur:[]) -> str:
    zero = ord('a')
    return ''.join([chr(code[0]+zero) for code in vecteur])

blocs_message_chiffre = decouper_message_en_bloc(message_chiffre)
vecteurs_chiffres_a_retrouver = [encoder_bloc_en_vecteur(bloc) for bloc in blocs_message_chiffre]

# --------------------------
# Brute force du chiffrement
# --------------------------
'''
Tous les cas possibles de blocs de 5 caractères sont chiffrés
Si on identifie un cas correspondant à un bloc du message chiffré, on l'enregistre
'''
matrice_chiffrement = np.array([[ 9,  4, 18, 20,  8],
                                [11,  0,  2,  1,  3],
                                [ 5,  6,  7, 10, 12],
                                [13, 14, 15, 16, 17],
                                [19, 21, 22, 23, 24]])
print(f'{matrice_chiffrement = }')



correspondance_blocs = {}
def enregistrer_correspondance(vecteur_chiffre:[], vecteur_en_clair:[]):
    bloc_chiffre = decoder_vecteur_en_bloc(vecteur_chiffre)
    bloc_en_clair = decoder_vecteur_en_bloc(vecteur_en_clair)
    correspondance_blocs[bloc_chiffre] = bloc_en_clair
    print(f'{bloc_chiffre} <- {bloc_en_clair}')

for i in range(25):
    for j in range(25):
        for k in range(25):
            for l in range(25):
                for m in range(25):
                    vecteur_en_clair = np.array([[i], [j], [k], [l], [m]])
                    vecteur_chiffre = matrice_chiffrement @ vecteur_en_clair % 25
                    if (vecteur_chiffre == vecteurs_chiffres_a_retrouver[0]).all():
                        enregistrer_correspondance(vecteur_chiffre, vecteur_en_clair)
                    elif (vecteur_chiffre == vecteurs_chiffres_a_retrouver[1]).all():
                        enregistrer_correspondance(vecteur_chiffre, vecteur_en_clair)
                    elif (vecteur_chiffre == vecteurs_chiffres_a_retrouver[2]).all():
                        enregistrer_correspondance(vecteur_chiffre, vecteur_en_clair)
                    elif (vecteur_chiffre == vecteurs_chiffres_a_retrouver[3]).all():
                        enregistrer_correspondance(vecteur_chiffre, vecteur_en_clair)
    #print(f'{i=}')
#print(i,j,k,l,m)


# ------------------------
# Déchiffrement du message
# ------------------------
message_en_clair = ''.join(correspondance_blocs[bloc] for bloc in blocs_message_chiffre)
print(f'{message_en_clair = }')
