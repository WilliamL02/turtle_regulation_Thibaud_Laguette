#### TP-1 Note : Turtle Regulation Package-INFO-2
##### Written by:
Ken Thibaud

Jean Alain William Laguette
la simulation de tortue est une simulation qui est faite afin de calculer l'angle de déplacement.

#### TURTLE REGULATION
Ce package permet de reguler le movement d'une autre tortue dans turtlesim en utilisant la regulation en cap et en distance.

Creation du launch File

Creez un fichier 'launch_file.launch' dans votre package

Ouvrez le fichier 'launch_file.launch' avec un editeur de texte.

#### Ajoutez le contenu suivant pour lancer tous les noeuds necessaires : 

Lancement du noeud set_way_point.py

```sh
<node name="set_way_point_node" pkg ="my_package" 
type="set_way_point.py" output="screen"/>
````

Lancement du noeud regulation_en_cap.py
```sh
<node name="regulation_en_cap_node" pkg="my_package" 
type="regulation_en_cap.py" output="screen"/>
```

Lancement du noeud regulation_en_distance.py

```sh
<node name="regulation_en_distance_node" pkg="my_package" 
type="regulation_en_distance.py" output="screen"/>
```

Lancement du noeud client.py

```sh
<node name="client_node" pkg="my_package"/>
```
