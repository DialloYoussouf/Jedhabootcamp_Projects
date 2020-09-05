### Prérequis: 
   Télécharger [Chromedriver](https://chromedriver.chromium.org/downloads) et l'ajouter au path de votre système.  
   
### Pour utiliser le Connecteur InstagramBot :
   Télécharger en local [le dossier ChromeDriver_Instagram](https://github.com/DialloYoussouf/Jedhabootcamp_Projects/edit/master/ChromeDriver_Instagram/)
   
   Ouvrir le fichier config.py (avec un editeur de texte par exemple) et remplacer 'your_instagram_username' et 'your_instagram_password' par vos identifiants instagram respectivement puis enregistrer
    
      username = 'your_instagram_username'
      password = 'your_instagram_password'
   
   Se déplacer dans le dossier ChromeDriver_Instagram grâce à la console et taper les commandes suivantes:
   
      python InstagramBot.py
      python config.py
      
   Ensuite vous pouvez maintenant ouvrir le [ChromeDriver_Instagram.ipynb](https://github.com/DialloYoussouf/Jedhabootcamp_Projects/blob/master/ChromeDriver_Instagram/ChromeDriver_Instagram.ipynb) 
   
   Amusez vous bien!

### Connecteur InstagramBot pour :
    Aller sur le site web d'Instagram  et de s'authentifier avec les identifiants et mot de passe fournis en argument.

    Aller sur le profil des utilisateurs et hashtag, et de les Follow (option par défaut).

    Parcourir, télécharger les posts & commentaires associés pour un utilisateur donné.
    
    Parcourir et Liker les posts d'un utilisateur.

#### Utilisation du module pymongo afin de stocker ces données (posts + dates + commentaires) sur une base de données mongoDB dans 3 collections différentes:
    Une première collection pour stocker les dates des posts
    Une seconde collection regroupant les urls menant à l'image de chaque post
    Une troisième collection rassemblant les commentaires pour chaque post 
    
   Les 3 collections étant reliées.
   

   

### Un accès utiisateur (droit de lecture) provisoire à cette base de donnée est crée également.

### Vous trouverez plus de detail dans le notebook dans lequel, j’ai fait une documentation sur l’utilisation du connecteur.

