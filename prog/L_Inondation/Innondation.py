'''
nc challenges.404ctf.fr 31420
« Allez, vite, il y a une pile de photos assez importante à traiter,
comptes-moi le nombre de rhinos par photo. »
                ~c`°^)                                                                    ~c`°^)
                          ~c`°^)          ~c`°^)    ~c`°^)  ~c`°^)            ~c`°^)    ~c`°^)
                                                                                       ~c`°^)
  ~c`°^)          ~c`°^)    ~c`°^)  ~c`°^)                      ~c`°^)              ~c`°^)
                ~c`°^)  ~c`°^)                                 ~c`°^)
    ~c`°^)  ~c`°^)                                 ~c`°^)                   ~c`°^)
                  ~c`°^)    ~c`°^)                              ~c`°^)  ~c`°^)
      ~c`°^)               ~c`°^)                                                   ~c`°^)
                        ~c`°^)          ~c`°^)                          ~c`°^)
                            ~c`°^)               ~c`°^)     ~c`°^)      ~c`°^)      ~c`°^)
~c`°^)                  ~c`°^)       ~c`°^)     ~c`°^)      ~c`°^)      ~c`°^)        ~c`°^)
            ~c`°^)                              ~c`°^)                                  ~c`°^)
~c`°^)                  ~c`°^)                  ~c`°^)                      ~c`°^)  ~c`°^)
 ~c`°^)     ~c`°^)                                              ~c`°^)                ~c`°^)
~c`°^)      ~c`°^)      ~c`°^)                      ~c`°^)  ~c`°^)                      ~c`°^)
                          ~c`°^)        ~c`°^)                              ~c`°^)
                            ~c`°^)                              ~c`°^)      ~c`°^)        ~c`°^)
  ~c`°^)        ~c`°^)  ~c`°^)                      ~c`°^)                             ~c`°^)
    ~c`°^)                ~c`°^)        ~c`°^)      ~c`°^)                               ~c`°^)
              ~c`°^)                    ~c`°^)        ~c`°^)   ~c`°^)                ~c`°^)
  ~c`°^)                                  ~c`°^)   ~c`°^)                ~c`°^)
    ~c`°^)                             ~c`°^)        ~c`°^)  ~c`°^)       ~c`°^)     ~c`°^)
                  ~c`°^)   ~c`°^)                                        ~c`°^)     ~c`°^)
      ~c`°^)                         ~c`°^)       ~c`°^)                ~c`°^)          ~c`°^)
                 ~c`°^)                                     ~c`°^)
                          ~c`°^)     ~c`°^)     ~c`°^)          ~c`°^)
                         ~c`°^)                     ~c`°^)        ~c`°^)   ~c`°^)   ~c`°^)
  ~c`°^)     ~c`°^)                     ~c`°^)        ~c`°^)   ~c`°^)   ~c`°^)
 ~c`°^)                                   ~c`°^)            ~c`°^)          ~c`°^)  ~c`°^)
~c`°^)          ~c`°^)                 ~c`°^)   ~c`°^)          ~c`°^)              ~c`°^)
                                                                                    ~c`°^)
                                                ~c`°^)      ~c`°^)      ~c`°^)
Combien de rhinocéros comptez-vous dans cette image ?
Votre réponse :
>
« Il faut compter plus rapidement, j'ai pas tout le temps du monde ! »
'''

from pwn import *

# Paramètres de connexion
HOST, PORT = "challenges.404ctf.fr", 31420

# Ouvre la connexion au serveur
io = remote(HOST, PORT)

# Forme du rhino
rhino = '~c`°^)'

# La question est posée 100 fois avant d'obtenir le flag
for i in range(100):
    #print('===============================================')
    #print(f'{i=}')
    #print('===============================================')
    message = io.recvuntil(b'> ')
    #print(message)
    nb_rhino = len(message.decode().strip().split(rhino)) - 1
    io.sendline(str(nb_rhino).encode())

# Récupération du flag dans le dernier message
dernier_message = io.recvall()
print(dernier_message.decode().strip())  

# Fermeture de la connexion
io.close()
