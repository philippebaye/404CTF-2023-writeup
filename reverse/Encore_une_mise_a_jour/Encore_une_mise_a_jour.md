# Encore une mise à jour !

<img alt="énoncé du challenge" src="enonce.png" width=500>

Le fichier fourni : [encore-une-mise-a-jour.py](encore-une-mise-a-jour.py)

En analysant le code on en déduit les éléments suivants :
- on doit fournir une chaine de 48 caractères
- cette chaine est transformée en un tableau dont les éléments sont les codes ASCII, en décimal, de chacun des caractères
- les éléments du tableau sont groupés 3 par 3 (c0, c1, c2), avant de vérifier la validité de 4 conditions/équations de la forme  :
  - équation 1 : c0 + c1 + cody*c2 == val1
  - équation 2 : c0 + c1 + cody*c2 == val2
  - équation 3 : c0 + cody*c1 + c2 == val3
  - équation 4 : c0 + cody*c1 + c2 == val4
- les équations sont, par construction, exclusives par paires :
  - équation 1 et équation 2, ne peuvent pas être vraies en même temps
  - idem pour équation 3 et équation 4
- si on saisit la bonne chaine de caractères, alors on a 32 équations qui sont vérifiées
  - donc pour chaque triplet (c0, c1, c2), on doit avoir 2 équations vraies parmi les 4.
  - autrement dit, en prenant les exclusions entre équations, pour chaque triplet :
    - equation 1 ou equation 2 doit être vraie
    - equation 3 ou equation 4 doit être vraie
- cody = `518` (pour cela, il suffit d'ajouter un `print(cody)` et d'exécuter le script)

En complément, la chaine est constituée de caractères imprimables (car on la saisit) :
  - on ne prend que les caractères standard ASCII
  - on en déduit que les caractères ont leur code ASCII sur la plage [32, 125]

----

La stratégie de résolution adoptée est la suivante :

- Pour toutes les combinaisons possibles de triplet (c0, c1, c2) on calcule la valeur de `c0 + c1 + cody*c2`.

- Si cette valeur est une valeur remarquable (i.e. une des valeurs utilisées dans les différentes équations 1 ou 2), on vérifie si `c0 + cody*c1 + c2` correspond elle aussi à l'une des valeurs des 2 équations 3 ou 4 associées.

- Si c'est le cas, le triplet (c0, c1, c2) fait partie de la chaine à retrouver.

L'algorihtme utilisé est implémenté dans le script [`encore-solution.py`](encore-solution.py) :

```bash
$ python3 encore.py
fragment n° 02 : -v4
fragment n° 14 : 22E
fragment n° 11 : 3S!
fragment n° 06 : 3ci
fragment n° 10 : CoD
fragment n° 00 : H!D
fragment n° 15 : ML8
fragment n° 13 : T5Y
fragment n° 09 : _0p
fragment n° 05 : _5p
fragment n° 07 : aLi
fragment n° 01 : d&N
fragment n° 04 : f0r
fragment n° 03 : r$_
fragment n° 08 : z3d
fragment n° 12 : |12
-------------------------------------
password = 'H!Dd&N-v4r$_f0r_5p3ciaLiz3d_0pCoD3S!|12T5Y22EML8'
```

Le flag est donc : `404CTF{H!Dd&N-v4r$_f0r_5p3ciaLiz3d_0pCoD3S!|12T5Y22EML8}`
