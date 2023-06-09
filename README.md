# C'est quoi le probleme du voyageur ?
Le problème est le suivant : un voyageur doit visiter toutes les villes, mais il a la flemme de marcher. Il veut donc réduire la distance totale de marche entre toutes les villes. Pour cela, il décide de créer un programme Python qui calcule le chemin le plus court pour lui. Cependant, un problème se pose : un algorithme qui calcule toutes les possibilités et retourne la meilleure solution a une complexité exponentielle par rapport au nombre de villes passées en paramètre. Par conséquent, il décide de créer un algorithme génétique.

Un algorithme génétique fonctionne selon les lois de la sélection naturelle. Il va donc garder les meilleures solutions au problème. Il ne va pas nécessairement retourner la meilleure solution, mais une solution qui s'en rapproche.

# Résultats du programme

le programme main.py execute le probleme du voyageur, il va d'abord crée N ville avec une matrice N*N représentant les distances entre les villes

par exemple cette matrice nous dit que la distance entre la ville N°1 et la ville N°3 est de 293,
ou encore que la distance entre la ville N°2 et la ville N°3 est de 201

 [[  0 158 293 309 391 333 273 105 409 125]  
  [158   0 201 289 172 227 244 453 376 302]  
  [293 201   0 303 190 157  86 345 290 402]  
  [309 289 303   0 191 284 234 200  46 225]  
  [391 172 190 191   0 186 405 195  93 163]  
  [333 227 157 284 186   0 409 243 378 198]  
  [273 244  86 234 405 409   0 466 238 375]  
  [105 453 345 200 195 243 466   0 177 150]  
  [409 376 290  46  93 378 238 177   0 122]  
  [125 302 402 225 163 198 375 150 122   0]]  


le programme va ensuite donné une solution au probleme 
par exemple ici la solution retenue
[[ 1  8 10  9  4  5  6  3  7  2]] 
le voyageur va passé dabors par la ville N°1 puis N°8 puis N°10 ect

le programme donne également un score(somme des distances) du résultat avec un comparatif du score moyen que l'on pourais avoir en parcourant au pif les villes
avec un score de [1201] l'esperance est de  2695.0

## remarque
 Les villes existent dans un univers parallèle au nôtre avec beaucoup plus de dimensions. C'est pourquoi il peut y avoir des incohérences si l'on regarde les résultats de mon générateur de distance sur un plan en 2D. Cependant, ici, l'algorithme fonctionne aussi bien en 1D que en (+inf)D

# Comment marche le programme

1. la fonction carto() va crée la carte des distance entre les villes.

2. la fonction populat() va crée des solutions valide de depart.

3. les fonctions selectElit() et selectTourn() sont deux méthodes de sélection. La première sélectionne uniquement les 50 % meilleurs individus, tandis que la seconde permet aux solutions de qualité inférieure d'avoir le chance de rivaliser entre elles et avec un peu de chance, de survivre.

4. la fonction calculAdapt() retourne le score d'une solution.

5. la fonction croisement() va croisé deux solutions entre elle pour en retourner deux autres, 
en gardant ~50% de génes de chaque solution.

6. la fonction mutation() elle va créer des changements de gènes comparables à ceux observés chez les habitants du nord.

7. enfin la fonction genetiq() elle est la fonction principale du programme. Elle prend différents paramètres (documentés dans le code) et renvoie une solution possible.