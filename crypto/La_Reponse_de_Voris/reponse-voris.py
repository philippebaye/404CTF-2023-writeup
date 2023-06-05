import sympy as sp


# Le message à déchiffrer
message_chiffré = 'pvfdhtuwgbpxfhocidqcznupamzsezp'

# Dimension du problème
dimension = len(message_chiffré)
print(f'{dimension = }')


# --------------------------
# Phase exploratoire de test 
# --------------------------
'''
{ ~ }  » nc challenges.404ctf.fr 31682
Bienvenue dans loracle, qui chiffre ce que vous rentrez. Vous devez dechiffrer : pvfdhtuwgbpxfhocidqcznupamzsezp
message en clair : aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa
message chiffre  : gvshnmijdwalablggmejiqvrhkixhns

message en clair : aaaaaaaaaaaaaaaaaaaaaaaaaaaaaab
message chiffre  : hwtionjkexbmbcmhhnfkjrwsiljyiot

message en clair : aaaaaaaaaaaaaaaaaaaaaaaaaaaaaba
message chiffre  : hxujpoklfycncdniioglksxtjmkzjpu

...

message en clair : abaaaaaaaaaaaaaaaaaaaaaaaaaaaaa
message chiffre  : hxvlssprmglxnpawxexddmspgkjzkrw

message en clair : baaaaaaaaaaaaaaaaaaaaaaaaaaaaaa
message chiffre  : hxvlssprmglxnpawxexddmspgkjzkrx

'''

mapping_message_enclair_chiffré = [
    ('aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa', 'gvshnmijdwalablggmejiqvrhkixhns'),
    ('aaaaaaaaaaaaaaaaaaaaaaaaaaaaaab', 'hwtionjkexbmbcmhhnfkjrwsiljyiot'),
    ('aaaaaaaaaaaaaaaaaaaaaaaaaaaaaba',	'hxujpoklfycncdniioglksxtjmkzjpu'),
    ('aaaaaaaaaaaaaaaaaaaaaaaaaaaabaa',	'hxvkqplmgzdodeojjphmltyuknlakqv'),
    ('aaaaaaaaaaaaaaaaaaaaaaaaaaabaaa',	'hxvlrqmnhaepefpkkqinmuzvlomblrw'),
    ('aaaaaaaaaaaaaaaaaaaaaaaaaabaaaa', 'hxvlsrnoibfqfgqllrjonvawmpncmsx'),
    ('aaaaaaaaaaaaaaaaaaaaaaaaabaaaaa', 'hxvlssopjcgrghrmmskpowbxnqodnty'),
    ('aaaaaaaaaaaaaaaaaaaaaaaabaaaaaa', 'hxvlsspqkdhshisnntlqpxcyorpeouz'),
    ('aaaaaaaaaaaaaaaaaaaaaaabaaaaaaa', 'hxvlssprleitijtooumrqydzpsqfpva'),
    ('aaaaaaaaaaaaaaaaaaaaaabaaaaaaaa', 'hxvlssprmfjujkuppvnsrzeaqtrgqwb'),
    ('aaaaaaaaaaaaaaaaaaaaabaaaaaaaaa', 'hxvlssprmgkvklvqqwotsafbrushrxc'),
    ('aaaaaaaaaaaaaaaaaaaabaaaaaaaaaa', 'hxvlssprmglwlmwrrxputbgcsvtisyd'),
    ('aaaaaaaaaaaaaaaaaaabaaaaaaaaaaa', 'hxvlssprmglxmnxssyqvuchdtwujtze'),
    ('aaaaaaaaaaaaaaaaaabaaaaaaaaaaaa', 'hxvlssprmglxnoyttzrwvdieuxvkuaf'),
    ('aaaaaaaaaaaaaaaaabaaaaaaaaaaaaa', 'hxvlssprmglxnpzuuasxwejfvywlvbg'),
    ('aaaaaaaaaaaaaaaabaaaaaaaaaaaaaa', 'hxvlssprmglxnpavvbtyxfkgwzxmwch'),
    ('aaaaaaaaaaaaaaabaaaaaaaaaaaaaaa', 'hxvlssprmglxnpawwcuzyglhxaynxdi'),
    ('aaaaaaaaaaaaaabaaaaaaaaaaaaaaaa', 'hxvlssprmglxnpawxdvazhmiybzoyej'),
    ('aaaaaaaaaaaaabaaaaaaaaaaaaaaaaa', 'hxvlssprmglxnpawxewbainjzcapzfk'),
    ('aaaaaaaaaaaabaaaaaaaaaaaaaaaaaa', 'hxvlssprmglxnpawxexcbjokadbqagl'),
    ('aaaaaaaaaaabaaaaaaaaaaaaaaaaaaa', 'hxvlssprmglxnpawxexdckplbecrbhm'),
    ('aaaaaaaaaabaaaaaaaaaaaaaaaaaaaa', 'hxvlssprmglxnpawxexddlqmcfdscin'),
    ('aaaaaaaaabaaaaaaaaaaaaaaaaaaaaa', 'hxvlssprmglxnpawxexddmrndgetdjo'),
    ('aaaaaaaabaaaaaaaaaaaaaaaaaaaaaa', 'hxvlssprmglxnpawxexddmsoehfuekp'),
    ('aaaaaaabaaaaaaaaaaaaaaaaaaaaaaa', 'hxvlssprmglxnpawxexddmspfigvflq'),
    ('aaaaaabaaaaaaaaaaaaaaaaaaaaaaaa', 'hxvlssprmglxnpawxexddmspgjhwgmr'),
    ('aaaaabaaaaaaaaaaaaaaaaaaaaaaaaa', 'hxvlssprmglxnpawxexddmspgkixhns'),
    ('aaaabaaaaaaaaaaaaaaaaaaaaaaaaaa', 'hxvlssprmglxnpawxexddmspgkjyiot'),
    ('aaabaaaaaaaaaaaaaaaaaaaaaaaaaaa', 'hxvlssprmglxnpawxexddmspgkjzjpu'),
    ('aabaaaaaaaaaaaaaaaaaaaaaaaaaaaa', 'hxvlssprmglxnpawxexddmspgkjzkqv'),
    ('abaaaaaaaaaaaaaaaaaaaaaaaaaaaaa', 'hxvlssprmglxnpawxexddmspgkjzkrw'),
    ('baaaaaaaaaaaaaaaaaaaaaaaaaaaaaa',	'hxvlssprmglxnpawxexddmspgkjzkrx'),
]


# -----------------------------------------------------------
# Transcription du chiffrement sous forme de calcul matriciel
# -----------------------------------------------------------
# Détermination de la base 
# (ie le décalage obtenu entre le message en clair composé uniquement de 'a' et le message chiffré correspondant
base_enclair, base_chiffrée = mapping_message_enclair_chiffré[0]
vecteur_base = sp.Matrix(dimension, 1, [ord(base_chiffrée[i])-ord(base_enclair[i]) for i in range(dimension)])
print(f'{vecteur_base = }')

# Détermination de la matrice de chiffrement, en base 26
delta = []
for texte_enclair, texte_chiffré in mapping_message_enclair_chiffré[1:]:
    delta.append([(ord(texte_chiffré[i]) - ord(texte_enclair[i])) % 26 for i in range(dimension)] )
matrice_chiffrement = sp.Matrix(delta[::-1]).T
print(f'{matrice_chiffrement = }')

# Calcul de la matrice de déchiffrement
# Comme c'est un peu long, on ne le fait qu'une fois. Ensuite on réutilise directement le résultat
#matrice_dechiffrement = matrice_chiffrement.inv_mod(26)
matrice_dechiffrement = sp.Matrix([[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 25, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 25, 2, 25], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 25, 2, 25, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 25, 2, 25, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 25, 2, 25, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 25, 2, 25, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 25, 2, 25, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 25, 2, 25, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 25, 2, 25, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 25, 2, 25, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 25, 2, 25, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 25, 2, 25, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 25, 2, 25, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 25, 2, 25, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 25, 2, 25, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 25, 2, 25, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 25, 2, 25, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 25, 2, 25, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 25, 2, 25, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 25, 2, 25, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 25, 2, 25, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 25, 2, 25, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 25, 2, 25, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 25, 2, 25, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 25, 2, 25, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 25, 2, 25, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 25, 2, 25, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 25, 2, 25, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 25, 2, 25, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [25, 2, 25, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [2, 25, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]])
print(f'{matrice_dechiffrement = }')


# -----------------------------
# Fonctions d'encodage/décodage 
# -----------------------------
def encoder_message_en_vecteur(message:str) -> []:
    zero = ord('a')
    return sp.Matrix(dimension, 1, [ord(c)-zero for c in message])


def decoder_vecteur_en_message(vecteur:[]) -> str:
    zero = ord('a')
    return ''.join([chr(code[0]+zero) for code in vecteur])


# ------------------------
# Déchiffrement du message
# ------------------------
# Le message à déchiffrer
print(f'{message_chiffré = }')

vecteur_chiffré = encoder_message_en_vecteur(message_chiffré)
vecteur_enclair = (matrice_dechiffrement * (vecteur_chiffré - vecteur_base) % 26).tolist()
message_enclair = decoder_vecteur_en_message(vecteur_enclair)
print(f'{message_enclair = }')
