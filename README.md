## Résumé

Site web d'Orange County Lettings

## Développement local

### Prérequis

- Compte GitHub avec accès en lecture à ce repository
- Git CLI
- SQLite3 CLI
- Interpréteur Python, version 3.6 ou supérieure

Dans le reste de la documentation sur le développement local, il est supposé que la commande `python` de votre OS shell exécute l'interpréteur Python ci-dessus (à moins qu'un environnement virtuel ne soit activé).

### macOS / Linux

#### Cloner le repository

- `cd /path/to/put/project/in`
- `git clone https://github.com/OpenClassrooms-Student-Center/Python-OC-Lettings-FR.git`

#### Créer l'environnement virtuel

- `cd /path/to/Python-OC-Lettings-FR`
- `python -m venv venv`
- `apt-get install python3-venv` (Si l'étape précédente comporte des erreurs avec un paquet non trouvé sur Ubuntu)
- Activer l'environnement `source venv/bin/activate`
- Confirmer que la commande `python` exécute l'interpréteur Python dans l'environnement virtuel
`which python`
- Confirmer que la version de l'interpréteur Python est la version 3.6 ou supérieure `python --version`
- Confirmer que la commande `pip` exécute l'exécutable pip dans l'environnement virtuel, `which pip`
- Pour désactiver l'environnement, `deactivate`

#### Exécuter le site

- `cd /path/to/Python-OC-Lettings-FR`
- `source venv/bin/activate`
- `pip install --requirement requirements.txt`
- `python manage.py runserver`
- Aller sur `http://localhost:8000` dans un navigateur.
- Confirmer que le site fonctionne et qu'il est possible de naviguer (vous devriez voir plusieurs profils et locations).

#### Linting

- `cd /path/to/Python-OC-Lettings-FR`
- `source venv/bin/activate`
- `flake8`

#### Tests unitaires

- `cd /path/to/Python-OC-Lettings-FR`
- `source venv/bin/activate`
- `pytest`

#### Base de données

- `cd /path/to/Python-OC-Lettings-FR`
- Ouvrir une session shell `sqlite3`
- Se connecter à la base de données `.open oc-lettings-site.sqlite3`
- Afficher les tables dans la base de données `.tables`
- Afficher les colonnes dans le tableau des profils, `pragma table_info(Python-OC-Lettings-FR_profile);`
- Lancer une requête sur la table des profils, `select user_id, favorite_city from
  Python-OC-Lettings-FR_profile where favorite_city like 'B%';`
- `.quit` pour quitter

#### Panel d'administration

- Aller sur `http://localhost:8000/admin`
- Connectez-vous avec l'utilisateur `admin`, mot de passe `Abc1234!`

### Windows

Utilisation de PowerShell, comme ci-dessus sauf :

- Pour activer l'environnement virtuel, `.\venv\Scripts\Activate.ps1` 
- Remplacer `which <my-command>` par `(Get-Command <my-command>).Path`

## Variables d'environement :
Le projet utilise 2 variables d'environement (secret key de django et DSN de sentry) stockées dans le fichier ".env" , non enregistré sur git hub.
Vous aurez besoin de créer ce fichier à la racine du projet pour executer l'application.

Le fichier doit contenir les variables suivante :
```
SECRET_KEY=fp$9^593hsriajg$_%=5trot9g!1qa@ew(o-1#@=&4%=hp46(s
SENTRY_DSN=https://84ad9cce424c4b9ab9980f910a0bcafe@o1186453.ingest.sentry.io/6306344
```

## Déploiement
Le déploiement est complétement automatisé, à chaque push sur la branche master, le pipeline s'execute sur circleCI, et est consultable ici : [https://app.circleci.com/pipelines/github/Nicolas-Frenay/P13_scalling?filter=all](url)

Le pipeline execute automatiquement les tests (flake8 et pytest), si les tests sont réussis, il créer une image docker et la push sur le dockerhub (nicolasfrenay/p13:latest), et enfin si la conteneurisation s'est bien effectuée, il déploie le projet sur heroku. [https://oc-lettings-nf.herokuapp.com/](url)

En cas de push sur une autre branche que master, il execute seulement les tests.

Les erreurs de l'application peuvent être suivi sur sentry (vous devez disposé d'un compte et avoir acces au projet) : [https://sentry.io/organizations/nf-1y/issues/?project=6306344](url)


### Configuration requise pour le déploiement :

- avoir cloner le projet depuis github
- être autorisé à effectuer des pushs sur le repository

Le pipeline étant totalement automatisé, aucune configuration supplémentaire n'est nécessaire



