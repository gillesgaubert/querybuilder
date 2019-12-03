readme : scriptRequete.py     auteur : gilles gaubert
-------------------------

Contexte : permettre de transformer un fichier contenant des id Salesforce issus d'une extraction avec un id par ligne en un fichier ou les id sont en une seule ligne de la forme:
'xxxxxid1','xxxxxid2',...
Avec des fichier de taille definissable par l'utilisateur (dataloader ne prends par exemple pas plus de 20000 caracteres dans les requetes).
Dans le cas ou la quantite est superieurs les donnees seront decoupees en plusieurs fichiers de sortie.

Prerequis : le script etant en python il faut avoir préalablement installé python 3 telechargeable sur python.org.

Utilisation :
fichier en entree : extract.txt
fichier(s) en sortie : out0.txt, out1.txt, ... dans le dossier 'out'
2 arguments a passer en ligne de commande : maxBuffer et idLength, par exemple à executer dans la ligne de commande :
python queryBuilder.py 15000 15
15000 et 15 sont prises par defaut si les arguments sont absents
