# Le Mystère du roman d'amour

<img alt="énoncé du challenge" src="enonce.png" width=500>

Le fichier fourni : [fichier-etrange.swp](fichier-etrange.swp)

On commence par analyser le type de fichier fourni :

```bash
$ file fichier-etrange.swp
fichier-etrange.swp: Vim swap file, version 7.4, pid 168, user jaqueline, host aime_ecrire, file ~jaqueline/Documents/Livres/404 Histoires d'Amour pour les bibliophiles au coeur d'artichaut/br
```

On obtient 3 des informations recherchées :
- PID du processus crashé = `168`
- Nom utilisateur = `jaqueline`
- Nom de la machine = `aime_ecrire`

Comme il s'agit d'un fichier SWAP VIM, on tente de le restaurer :

```bash
$ vim -r fichier-etrange.swp

Using swap file "fichier-etrange.swp"
Original file "~jaqueline/Documents/Livres/404 Histoires d'Amour pour les bibliophiles au coeur d'artichaut/brouillon.tx"~jaqueline/Documents/Livres/404 Histoires d'Amour pour les bibliophiles au coeur d'artichaut/brouillon.txt" [New DIRECTORY]
Recovery completed. You should check if everything is OK.
(You might want to write out this file under another name
and run diff with the original file to check for changes)
You may want to delete the .swp file now.

Press ENTER or type command to continue

<89>PNG^M
^Z
^@^@
...
```

On obtient une nouvelle information recherchée :
- Chemin d'origine du fichier = `~jaqueline/Documents/Livres/404 Histoires d'Amour pour les bibliophiles au coeur d'artichaut/brouillon.txt`

D'après l'entête du fichier, il s'agit d'un PNG. On l'enregistre donc comme tel :
```vim
:x! recover.png
```

> NB : On peut récupérer directement le fichier, sans l'ouvrir :
> ```bash
> $ vim -r fichier-etrange.swp -c ':x! recover.png'
> ```

Il s'agit bien d'une image, mais sans information particulière :

<img alt="fichier restoré" src="recover.png" width=500>

Par contre, si on ouvre le fichier avec stegsolve, une des vues (notamment "Blue Plane 0") fait apparaître une image tout autre :

<img alt="fichier restoré dans stegsolve" src="recover-blue_plane_0.bmp" width=500>

Le QRCode correspond au texte suivant (obtenu pour ma part via l'application de mon smartphone) :

```txt
Il était une fois, dans un village rempli d'amour, deux amoureux qui s'aimaient... Bien joué ! Notre écrivaine va pouvoir reprendre son chef-d'oeuvre grâce à vous ! Voici ce que vous devez rentrer dans la partie "contenu du fichier" du flag : 3n_V01L4_Un_Dr0l3_D3_R0m4N
```

On obtient la dernière information recherchée :
- Contenu du fichier = `3n_V01L4_Un_Dr0l3_D3_R0m4N`

On utilise les différentes informations collectées pour reconstituer le flag : `404CTF{168-~jaqueline/Documents/Livres/404 Histoires d'Amour pour les bibliophiles au coeur d'artichaut/brouillon.txt-jaqueline-aime_ecrire-3n_V01L4_Un_Dr0l3_D3_R0m4N}`
