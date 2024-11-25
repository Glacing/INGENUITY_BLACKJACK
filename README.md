# INGENUITY_BLACKJACK
Court projet réalisé dans le cadre du cours d'Interaction Distribuée à l'UPSSITECH

L'objectif était d'implémenter le jeu de Blackjack au travers des outils proposés par l'entreprise Ingenuity, et plus particulièrement à l'aide de Ingescape ainsi que du Whiteboard.
Nous avons eu seulement 3 séances de 2 heures pour travailler sur ce projet, d'où le "court" projet.

A ce stade, le jeu supporte 2 joueurs s'affrontant en 1 contre 1. 

La version actuelle est très simplifiée ;
- les joueurs n'ont pas de solde, la gestion de la mise et du gain n'est alors pas supportée.
- les joueurs jouent tour à tour.
- l'affichage se fait à l'aide de l'outil Whiteboard, ce dernier n'étant pas interactif dans cette version.

# Lancer le blackjack
Il est possible de lancer l'application de deux façons : 
1. Lancer les agents dans des terminaux séparés
Ouvrir quatre terminaux de le repertoire où sont stockés les agents et y réaliser les commandes :
```
python3 Gestionnaire\main.py Gestionnaire Wi-Fi 5670
python3 Pioche\main.py Pioche Wi-Fi 5670
python3 Joueur\main.py J1 Wi-Fi 5670
python3 Joueur\main.py J2 Wi-Fi 5670
```

2. Utiliser le script
Dans le fichier racine des agents est disponible un script launch.batch, vous devez l'éditer et modifier la ligne 35 pour mettre le lien d'exécution du whiteboard sur votre pc.
```
start "" "C:\Users\aurel\Downloads\Whiteboard.win64\Whiteboard\Whiteboard.exe"
```
Une fois cela fait, vous pouvez exécuter le script depuis un terminal avec cette commande : 
```
.\launch.bat
```
# Joueur au blackjack
Depuis l'application, vous pouvez appeler le service "lancerPartie" de Gestionnaire pour démarrer une nouvelle partie de blackjack.
Par la suite, il suffit d'appeler les services de J1 et J2 en fonction de si vous souhaitez tirer une carte ou arrêter de tirer.
Une fois la partie finie, vous pouvez à nouveau appeler lancerPartie pour en commencer une nouvelle.
