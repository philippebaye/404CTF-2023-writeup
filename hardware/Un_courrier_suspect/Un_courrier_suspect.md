# Un courrier suspect

<img alt="énoncé du challenge" src="enonce.png" width=500>

Le fichier fourni : [bienvenue.circ](bienvenue.circ)

On ouvre le fichier fourni avec [Logisim](http://www.cburch.com/logisim/) qui montre 4 parties.

partie_1 :
- le texte contient le début du flag `404CTF{L3_`

partie_2 :
- on lance la simulation et on obtient à l'affichage digital : `4d306d33 6e545f33 53745f56 336e555f`
- un décodage hexa donne : `M0m3nT_3St_V3nU_`

partie_3 :
- on rentre le résultat obtenu à la partie 2 dans la ROM
- puis on lance la simulation
- on obtient `M0m3nT_3St_V3nU_` :smile:

partie_4 :
- le schéma ressemble à la partie_2, mais elle fait appel à partie_4_blackbox (qui ne récupère que le bit de poids faible)
- si on lance la simulation l'affichage digital n'est pas très satisfaisant.
- mais si on récupère les entrées, comme sur la partie_2, on obtient `44335f35 346d7573 33727d00 00000000`
- un décodage hexa donne : `D3_54mus3r}`

En mettant bout à bout les différents morceaux, on reconstitue le flag : `404CTF{L3_M0m3nT_3St_V3nU_D3_54mus3r}`
