# Git & Github

## Git

### C'est quoi ?

* Logiciel de contrôle de version (VCS) (Voir les anciennes versions du code)
* Inclure des messages de versions et des descriptions
* Créer des branches et travailler à plusieurs dessus
* Mettre des balises (tag) sur certaines versions
* En local et peut-être envoyée sur un dépôt distant

### Différents niveaux de travail

* **Arbre de travail (working tree)**: Ensemble de répertoires et de fichiers imbriqués qui contiennent le projet sur lequel on travaille.

* **Dêpot (repository)**

  * Niveau supérieur d’un working tree
  * Git y conserve tout l’historique et les métadonnées du projet

* **Bare repository**

  * Dépôt nu, est partagé ou backup, appartient pas working tree
  * Répertoire avec un nom qui se termine par .git

### Définitions

* Commit: Commettre changements qu’on a apporté, pour que tout le monde puisse les voir (snapshot du code à un moment donné)
* Branch:
  * Série de commit liés
  * Permet de travailler de manière indépendante sur le code, permet d'être fusionnée avec une autre branche quand une fonctionnalité est finie
  * La branche par défaut est appelée main ou master (ancienne appelation)
* Remote - dépôt distant: Nom du répertoire distant: appelé origin par git, remote par défaut

### Commandes

Les [] sont à remplacer par le contenu.  

#### Configuration de base

* git config --global user.name "[USER_NAME]"
* git config --global user.email "[USER_EMAIL]"

#### Commandes principales

* git init -> Initier git dans un dossier
* git add [nom fichier] ou .  -> Ajoute les fichiers dans l'index, git les suit, si ils ne sont pas suivis: "U" pour "Untracked" (. -> Permet d'ajouter tous les fichiers)
* git commit -m "[message de commit]" -> Crée un snapshot des fichiers ajouter avec git add
* git push origin [nom branche] -> Envoyer les fichiers dans le dépôt distant (GitHub)
* git pull origin [nom branche] -> Récupérer les changements du dépôt distant (GitHub)
* git status -> Voir les changements effectués et les fichiers suivis ou non suivis par git
* git branch [nom branche] -> Permet de créer une branche
* git branch -> Voir les branches et celle sur laquelle on se trouve
* git checkout -> Changer de branche
* git merge -> Fusionner 2 branches
  * Pour fusionner: aller sur la branche où on veut fusionner, git merge [branche avec laquelle on veut fusionner]
* git rm [nom fichier] -> Supprimer un fichier

### Comment l'utiliser

* Dans le terminal de VScode ou dans son terminal cmd, powershell,... grâce aux lignes de commande
* Dans GitHub Desktop (Interface graphique), mais fonctionnalité limitées

### Bonnes pratiques

* Ajout d'un fichier ".gitignore" -> Permet de ne pas ajoute de fichiers inutiles ou sensibles, dossiers. Exemple: .venv/, .vscode/, log,...  
* Ajout d'un README.md qui explique le projet, l'installation,...
* Utiliser des conventions de nommage pour les branches, fichiers, messages de commit,... (Sera détaillé plus tard)

## Github

### C'est quoi ?

* Cloud permettant de stocker des dépôts git
* Facilite le travail en équipe
* Permet d'organiser des projets, écrire de la doc,...

### Comment l'utiliser ?

* Tout en GUI
* [Site de Github](https://github.com)
