# Oracle cassé

<img alt="énoncé du challenge" src="enonce.png" width=500>

Le fichier fourni : [oracle.py](oracle.py)

L'analyse de ce dernier montre une implémentation RSA-CRT (i.e. utilisant les restes chinois pour optimiser le calcul de la signature) somme toute classique.

La machine commence par fournir au démarrage un texte chiffré (dont l'objet du challenge consiste à en retrouver le contenu en clair).
Puis le module de chiffrement `n` utilisé.
Ensuite, nous avons la possibilité de fournir des données sur lesquelles l'algorithme de calcul de signature est appliqué.

Si le comportement de la machine est correct, on devrait avoir :

$$ Message = (Signature(Message))^{e} \ (\bmod\ n) $$

Et :

$$ Message\_clair = Signature(Message\_chiffré) \ (\bmod\ n) $$

On teste donc le comportement de la machine en lui demandant de calculer la signature du message chiffré `ct` fourni au démarrage :

```bash
$ nc challenges.404ctf.fr 31674
Bienvenue dans notre nouveau service d'oracle!
Le service de l'année précédente nous a causé de nombreaux problèmes, il ne fonctionnait pas comme attendu et était inefficace.
C'est pourquoi nous avons décidé de tout reprendre à zéro! Cette fois un seul oracle est présent, et il a été optimisé pour être le plus efficace possible!
Pour fêter le lancement de ce nouveau service, nous offrons un cadeau aux mille premiers utilisateurs.
...........................................................................................................................................................
Félicitations! Vous faîtes parti des mille premiers! Voici votre bon-cadeau à utiliser dans l'oracle!:
19954536137413049069725718632123144876938322782619680025138760809743495713774446207599950812214925688838997564709564783874636462771109910828227532928174946396436076056918137882599342425488189697565682358447872011141574458576698323687234927675062102869280613805755040835958128735008189935094221432445596510906003637991674938536551749230332118770696614695221247111685317395224057030148152399448834011029615507535803650928452682971341488508630023397534467553806440954006621846770602307061783799843460348520792472644136850167742989439963135091580862087127928831789352235009034446517642590812669379790193107164799607142199
Initialisation de l'oracle n°0xc26c5658fe724e724f128b4a374bb1f99f50861c959d12b400a7bfc95e850c1c332e85ae2b45c2aaca7751ab59bc77ae3de6f5f1dfe2e2c7ca3148ed7030c9837b4088b450614160adffa388d863b5c15f1c873cca8b173152b370eea30e71f75b8bcd8a19729bb80850dc01d8f42b9d5c7343120924690de73b61251d31a53a3a16e011d4e3eb15c5b5d5a3553f89ed3a4d6d0c13d19c3a741dfb12b77b257b98f6d5c1d36315a04df63324cb57373c9638f7cc9e16e4299a64de5c11a50d6c19b12802a27dafbea5f8d46c46bcd8b2fc621fda6a693347c52edea16d191f7b7277865df14c2f5cd3046d700b03328df55ffce435069b4cd68a56c702cec91f terminée. Bonne utilisation!
Que voulez vous envoyer à l'oracle?
19954536137413049069725718632123144876938322782619680025138760809743495713774446207599950812214925688838997564709564783874636462771109910828227532928174946396436076056918137882599342425488189697565682358447872011141574458576698323687234927675062102869280613805755040835958128735008189935094221432445596510906003637991674938536551749230332118770696614695221247111685317395224057030148152399448834011029615507535803650928452682971341488508630023397534467553806440954006621846770602307061783799843460348520792472644136850167742989439963135091580862087127928831789352235009034446517642590812669379790193107164799607142199
17144131568611544923924884117149141141948607698871432583524322994388188895817862747946817335233528390478646775940133631708639280395207181507389357229038329877161519985389549570992309434991988223802462946696478593821096221012801154569192196406096811043575701914549932051487719576485351105921305787858713752637215902619522029326167376082406665962547715920097288752959585296389895068599477674951519077862202378532752064805649845769039000216361672920963485602232065196309327645211835813295389700317869926869231025160249503972392564694904334791072796301810377270443089294098961958239656638432529486157922526655559022979795
Que voulez vous envoyer à l'oracle?
```

On constate que la machine est "cassée", car le comportement n'est pas celui auquel on s'attend.

On suppose un problème dans l'exponentiation modulaire, dont on va se servir comme dans une attaque par faute de Bellcore.

L'algorithme est implémenté dans le script [`oracle-reverse.py`](oracle-reverse.py) :

```bash
$ python3 oracle3.py
1er GIFT candidat : b'\x87\xce\xc4>@|M\x7f\xfe\xc0\x9a8~\xca\xa7,\x83\x8d\x9d\xab\xc8\xc5\xf1\xa5\x12\x88\x99|kN\x88\x88\xd8\xf7\xa2|\xddv8C\xed\x8e\x94\xa6\xd7\xb4|@!\x04\xce\xaf\xbf`Z\x04\xc7\x93\xb7,/\x8cc\xa0;\xb8I#\xd4\x10 \xf2\xc6\xd6\xaf9\xc6Fr\x99sS+Z\xa8\x06\xd0\xf2O\x82M\x7fK^\x18\xe3an\t\xfa82\x1f\x0f)>\xef\x88\x05\xe3\tS\x86z?H\xf0AQ\xad\xe1\xe1=gv\xf0\xbf\x9a\xe2\x9d\xf9\xe0\xb9\xb7\xb1L\xe4\n3\x80\x17\x98\x16\x0c\x9et\xb6\x14/\xa0\x8d\xdaH\xf6D\x8f#h\xae\t."\xe3\x10U\xddq>\x00\xad\xb8i\x0f\\\xbb\xbf\xb0\x1e\x9f\xec\x93\xbc\xa9h\xf6\x1fQ\xfa]C\xf3\xc2\x01\xb9\xa8\xcdau\x1f\xd5\xc4\xc0#\x03\xf9P\xe1\xc2\x9eaFJg.2\x11\x13*6\xe4\xc9\x04\x1c\x84\xdc3\x85N\x90x\x01Y\xa3*S\x84\xed\xf6Zf\xb3B\xaa3W9\xe7\xa5\xfcH=\x86>\xd4\xaa\xd3'
---------------------------
2eme GIFT candidat : b'Bonjour,\nVoici le cadeau auquel vous avez droit: 404CTF{Un_0r4cl3_vr41m3n7_c4553_c3773_f015}\nEn nous excusant pour la gene occasionnee,\nLa direction'
```

Le flag est donc : `404CTF{Un_0r4cl3_vr41m3n7_c4553_c3773_f015}`
