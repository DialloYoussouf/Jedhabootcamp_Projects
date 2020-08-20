## Connecteur capable de se connecter à Instagram avec les identifiants et mot de passe.
## Prérequis: installer Chromedriver et l'ajouter au path de votre système.  

Aller sur le profil des utilisateurs et hashtag, et de les Follow si l'argument Follow_hashtag ou Follow_Follow est True.
Il permet aussi de parcourir leur photos/posts, les télécharger ainsi que les commentaires associées et de liker toutes les photos si l'argument Like est True.
Ces données sont par la suite stockées sur une base de données mongoDB grâce au odule pymongo.
Une base de donnée utiisateur KaisensDataDB est disponible afin de afin de faire des requêtes sur les collections.
Vous trouverez plus de detail dans le notebook dans lequel, j’ai fait une documentation sur l’utilisation du connecteur.

