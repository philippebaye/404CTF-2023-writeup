import ascon

# -------------------
# Données de l'énoncé
# -------------------
clef = bytes.fromhex('00456c6c616e61206427416c2d466172')
print(f'{clef = }')

nonce = bytes.fromhex('00000000000000000000000000000000')

message_chiffré = bytes.fromhex('ac6679386ffcc3f82d6fec9556202a1be26b8af8eecab98783d08235bfca263793b61997244e785f5cf96e419a23f9b29137d820aab766ce986092180f1f5a690dc7767ef1df76e13315a5c8b04fb782')

données_associées = bytes.fromhex('80400c0600000000')

# -------------
# Déchiffrement 
# -------------
message_déchiffré = ascon.decrypt(clef, nonce, données_associées, message_chiffré, variant="Ascon-128")
print(f'----------------------')
print(f'message déchiffré brut = {message_déchiffré}')
print(f'----------------------')
print(f'message déchiffré en tenant compte de l\'encodage: \n{message_déchiffré.decode("iso8859")}')
