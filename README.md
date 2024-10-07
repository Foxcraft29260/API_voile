# Wind Finder
## **Utilisation du logiciel** :
- télécharger le fichier « weather_finder setup.exe » et l’exécuter.
 -Après l'installation, vous serez accueillies par une fenêtre comme si dessous en lanceant le programme :  
  ![img](https://github.com/user-attachments/assets/a7788f10-0004-489f-a60a-8e0b90f0c9a6)
- Le curseur a gauche va de 1 (en bas) a 5 (en haut), il permet de choisir le nombre de jour dans le futur pour récupérer les prévisions.
- L'entrée de texte (au centre en dessous de wanted city) permet de choisir la ville où récupérer les prévisions.
- Quand vous avez paramétré votre recherche, appuyez sur locate.
> [!CAUTION]
> Lancer un des fichiers `.py` sans les extensions pourrait entrainer des ereurs
## **Questions posées** :
- Comment récupérer les données selon des critères précis?(direction du vent, vitesse du vent, comment afficher les données récupérées)
- Par quel moyen les donner à l'utilisateur
- Comment faire en sorte que l’installation des modules nécessaires ne soit plus une étape obligatoire pour lancer le programme.
## **Fonctionnement du programme** :
- API utilisée: [weatherapi](https://www.weatherapi.com/)
### **Modules utilisés** :
- [**_requests_**](https://fr.python-requests.org/en/latest/) : pour executer les liens internets
- [**_tkinter_**](https://docs.python.org/fr/3/library/tkinter.html) : pour l'interface graphique
- [**_customtkinter_**](https://github.com/TomSchimansky/CustomTkinter) : pour un effet moderne a l'UI.
### **Trois fichiers séparés** :
- **_app.py_** : Ce fichier est la partie récupération de données du logiciel ; A l'aide du module requests, on exécute la commande de récupération de données au format json dans la plage horaire 8h/20h avec les spécifications de l’utilisateur (nombre de jours dans le futur, ville) et on exécute ensuite une suite de boucles if pour récupérer dans un tableau les éléments nécessaires et demandées par le l'utilisateur. Ce tableau est ensuite renvoyée vers le fichier menu.py qui s'occupera de formater toutes ces données pour les incruster dans une fenêtre customtkinter.
- **_Menu.py_** : Ce fichier s'occupe de l'aspect graphique du programme, il appele la fonction du fichier app.py pour récupérer les données de l'API et formatte le tout pour récupérer un rendu propre.
## **Problèmes rencontrées** :
- Le principal problème rencontré lors de ce projet a été de comprendre la structure des données renvoyées par l'API : toutes les données n'étant pas nécessaire, on a du étudier la structure du fichier pour récupérer les bons éléments et délaisser les éléments inutiles.
- Dans le cadre de l'UI, le problème a été de bien trier les informations reçues puis de les afficher de façon structurées. Ce problème à eu comme résultat une obligation de la restructuration de la récolte de données.
