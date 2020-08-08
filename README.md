# Ranger

## Description

Ranger est une application tres simple qui permet de ranger les fichiers en un clic.

L'application vient avec deux interfaces graphiques. L'une permet de customiser comme on le souhaite nos rangements tandis que la seconde nous laisse acceder a notre historique des rangements

## Installation:

- Ouvrir un **powershell en admin**
- Lancer la commande `python -m pip install -e .`


## Utilisation

Vous pouvez acceder aux differentes applications a partir du context menu (right click).

### Ranger

Cette option permet de ranger vos fichiers. Le comportement varie selon le type de fichier. Ce comportement sera mis a jour dans les prochaines versions, afin de correspondre le plus possible a votre facon de ranger vos fichiers.

![Ranger context menu](./assets/context_menu.png?raw=true "Title")

![Ranger console](./assets/ranger_console.png?raw=true "Title")


### Archive

L'application d'archive permet d'avoir acces a l'historique de nos fichiers.

Elle est compose de 3 colonnes et d'autant de ligne que l'on a de fichier. On peut annuler un rangement en faisant un clic droit sur la ligne que l'on veut annuler. On a alors deux options:
- Annuler le rangement de toute l'operation, c'est a dire tous les fichiers qui ont ete deplace en meme temps
- Annuler le rangement d'un seul fichier.

On peut egalement filtrer les colonnes grace aux input en haut de la page. Pour se faire, rien de plus simple, il te suffit de specifier ce que tu cherches dans l'input correspondant. Par exemple, si je ne veux voir que l'operation 0, je peux ecrire 0 dans la zone de texte en haut a gauche.

![Archive interface](./assets/interface_archive.png?raw=true "Title")

### Rules

Cette application est sans aucun doute l'une des plus importantes. C'est ici que vous choisissez des regles de rangement, permettant a l'application de mieux comprendre ou vous vouler ranger vos fichiers. Certaines regle existe deja par defaut. Il est tres facile pour vous de les modifier. Il vous suffit de cliquer sur la cellule que vous souhaitez modifier.

Le tableau present dans cette application est divise en 3 colonnes:
- **Key**: Il s'agit d'un element permettant d'identifier le fichier. Cela peut etre une partie du nom ou bien meme une information presente dans les fichiers metadata. 
- **Path**: c'est l'endroit ou vous voulez enregistrer le fichier contenant cette cle. Si jamais il existe plusieurs cle correspondant a votre fichier, la colonne priorite permettra de determiner le path final
- **Priority**: Permet de determiner quel path on met en priorite.

Vous avez egalement la possibilite d'ajouter de nouvelle ligne en descendant en bas du tableau. Il est important de ne pas oublier d'appuyer sur le bouton save afin d'enregistrer, que ce soit apres l'ajout d'une ligne ou de son edition.

![Rules interface](./assets/interface_rules.png?raw=true "Title")


## Test
Vous pouvez lancer les tests avec cette commande: 
`python -m pytest`

## Logs
Vous pouvez trouver le fichier de log ici:  `ranger/data/logging.log`

