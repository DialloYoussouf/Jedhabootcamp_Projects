### Prérequis: 
   Télécharger [Chromedriver](https://chromedriver.chromium.org/downloads) et l'ajouter au path de votre système.  

### Connecteur InstagramBot pour:
    Aller sur le site web d'Instagram  et de s'authentifier avec les identifiants et mot de passe fournis en argument.

    Aller sur le profil des utilisateurs et hashtag, et de les Follow (option par défaut).

    Parcourir, télécharger les posts & commentaires associés pour un utilisateur donné.
    
    Parcourir et Liker les posts d'un utilisateur.

### Utilisation du module pymongo afin de stocker ces données (posts + dates + commentaires) sur une base de données mongoDB dans 3 collections différentes:
    Une première collection pour stocker les dates des posts
    Une seconde collection regroupant les urls menant à l'image de chaque post
    Une troisième collection rassemblant les commentaires pour chaque post 
    
   Les 3 collections étant reliées.

### Un accès utiisateur (droit de lecture) provisoire à cette base de donnée est crée afin de afin de récupérer les données.

### Vous trouverez plus de detail dans le notebook dans lequel, j’ai fait une documentation sur l’utilisation du connecteur.

