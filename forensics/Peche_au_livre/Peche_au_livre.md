# Pêche au livre

<img alt="énoncé du challenge" src="enonce.png" width=500>

Le fichier fourni : [Capture.pcapng](Capture.pcapng)

On utilise Wireshark pour ouvrir le fichier `Capture.pcapng`.

On filtre, pour ne conserver que les requêtes HTTP :

![Uniquement les requêtes HTTP](wireshark-filter-http.png)

On sélectionne la 1ere trame HTTP, et on suit le flux (Click droit > Follow > HTTP Stream) :

![Requête vers /](wireshark-follow-http-stream.png)

La réponse fait apparaître 3 liens vers des fichiers.

Ces 3 fichiers ont bien été téléchargés :

![requêtes de téléchargement](wireshark-http-downloads.png)

On les exporte (File > Export Objects > HTTP)

Le flag est présent dans le fichier image `Hegel-sensei-uwu.png` :

![Fichier Hegel-sensei-uwu.png](Hegel-sensei-uwu.png)
