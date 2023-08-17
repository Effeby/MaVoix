# Projet MaVoix

Bienvenue dans le projet MaVoix ! Ce projet est une application web construite avec Django qui fournit une plateforme aux utilisateurs pour interagir avec différentes fonctionnalités.

## Démarrage

Suivez ces instructions pour mettre en marche le projet sur votre machine locale.

### Prérequis

- Python (3.7 ou supérieur)
- Django (4.2.4)
- Environnement virtuel (optionnel, mais recommandé)

### Installation

1. Clonez le dépôt sur votre machine locale :
   git clone https://github.com/votre-nom-utilisateur/projet-mavoix.git

Naviguez vers le répertoire du projet :
cd projet-Page

Créez un environnement virtuel (optionnel, mais recommandé) :
python -m venv venv

#Pour activer l'environnement virtuel
# Sur Windows, utilisez : venv\Scripts\activate   

Installez les dépendances du projet :
pip install -r requirements.txt

Exécutez les migrations de la base de données :
python manage.py migrate

Utilisation
Démarrez le serveur de développement :
python manage.py runserver

Un lien vers le site s'affichera et vous donnera acces au site.

Structure du Projet
Acceuil: Cette application contient les vues, les templates et autres ressources liées à l'interface utilisateur principale.
Accueil/urls.py: Configuration des URL pour le projet.
Page/settings.py: Paramètres Django pour le projet.
static/: Répertoire pour les fichiers statiques (CSS, JS, images).
templates/: Répertoire pour les templates HTML.





