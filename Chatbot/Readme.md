# Chatbot
   Chatbot pour répondre aux questions fréquemment posées (FAQ) sur le COVID-19. Source de données [OMS](https://www.who.int/fr/emergencies/diseases/novel-coronavirus-2019/advice-for-public/q-a-coronaviruses)

## Deux manières d'utiliser le chatbot:
### Voici le lien vers la version notebook du chatboot : [Google colab](https://github.com/DialloYoussouf/Jedhabootcamp_Projects/blob/master/Chatbot/Final_Chatbot.ipynb)

### Veuillez suivre les étapes ci-dessous afin d'utiliser le chatbot sur un pc en local (seconde méthode)
   Si vous n'avez pas Anaconda Navigator installé sur votre machine, [voici le lien de téléchargement](https://docs.anaconda.com/anaconda/install/) 

#### Télécherger tout le dossier Chatbot sur votre machine en local

#### Ouvrir une CLI (la console d'anaconda a été utilisée pour ce projet)
    Se déplacer dans le dossier Chatbot téléchargé précédemment

#### Créer un environnement virtuel *env* et y installer python=3.7 numpy=1.16.1
    conda create -n env python=3.7 numpy=1.16.1
    
   *env* étant le nom de l'environnement crée 

#### Activer cet environnement virtuel
    conda activate env

#### Installer les modules contenus dans le requirements.txt
    pip install -r requirements.text

#### Pour démarrer le chabot
    python final_chatbot.py

#### Le Chatbot est prêt
   [Voici des exemples de questions que vous pouvez poser au bot](https://www.who.int/fr/emergencies/diseases/novel-coronavirus-2019/advice-for-public/q-a-coronaviruses).
   
   Pour le moment, le bot est entrainé à ne répondre qu'à ces questions ci-dessus. 
   Il peut cependant, répondre aux salutions, remerciement et au revoir. 


#### Tapez *quit* pour fermer le chatbot

