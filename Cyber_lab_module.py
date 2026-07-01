import os
import time
import random
import sys
print("==OPERATION SANDBOX==")
print("."*40)
sys.argv[0]
if len (sys.argv) >1 :
    dossier_à_scanner= sys.argv[1]
    Mode= "Alerte"
else:
    Mode="Normal"
dossier_à_scanner="."
print("Lancement de l'inspection sur le dossier : ", ".")
print("." *40)
if os.path.exists (dossier_à_scanner):
   fichiers= os.listdir(dossier_à_scanner)
   compteur=0
   for f in fichiers:
    compteur+=1
    Choice=random.choice(fichiers)
    print("Le fichier à analyser au hasard est:", Choice)
    if Mode=="Normal":
     time.sleep(3)
   else:
    time.sleep(1)
else:
    print("ERROR, le dossier à scanner n'existe pas")
print("==Fin de l'analyse==")
print("Le dossier compte:", compteur, "fichiers")

   
