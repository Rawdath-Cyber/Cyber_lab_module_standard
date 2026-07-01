# Cyber_lab_module_standard
Description
Ce projet a été réalisé dans le cadre de mon parcours d'apprentissage en cybersécurité et en automatisation avec Python.
L'objectif de ce laboratoire pratique était de combiner plusieurs modules standards de Python afin de simuler une opération d'inspection automatisée dans un environnement de sécurité informatique.
Le script reproduit le comportement simplifié d'un outil d'analyse capable d'adapter sa vitesse d'exécution selon un niveau d'alerte.
Objectifs pédagogiques
Ce projet m'a permis de pratiquer :
Le module sys
Le module os
Le module random
Le module time
Les structures conditionnelles
La manipulation de fichiers et dossiers
L'automatisation de tâches simples
Fonctionnement
Le script réalise les opérations suivantes :
1. Vérification du mode d'exécution
Le programme vérifie si un argument a été fourni lors du lancement :
Aucun argument → Mode Standard
Argument détecté → Mode Alerte
2. Analyse du dossier courant
Le script parcourt le dossier actuel et compte le nombre total de fichiers présents.
3. Sélection aléatoire
Parmi les fichiers détectés, un fichier est choisi aléatoirement afin de simuler une analyse approfondie.
4. Simulation d'inspection
Le temps d'attente varie selon le mode sélectionné :
Mode
Temps d'attente
Standard
3 secondes
Alerte
1 seconde
Une fois l'attente terminée, le fichier sélectionné est affiché.
Technologies utilisées
Python 3
Module os
Module sys
Module random
Module time
Exemple d'utilisation
Lancement en mode standard :
python cyberlab_module.py
Lancement en mode alerte :
python cyberlab_module.py alerte
Compétences développées
Automatisation de tâches
Gestion de l'environnement système
Utilisation des arguments en ligne de commande
Simulation de scénarios de cybersécurité
Organisation logique d'un script Python
Contexte d'apprentissage
Projet réalisé dans le cadre de mon objectif personnel :
🎯 Maîtriser l'ensemble des compétences de niveau débutant en cybersécurité avant la rentrée universitaire.
Ce laboratoire fait partie de mon parcours documenté sur GitHub et LinkedIn.
