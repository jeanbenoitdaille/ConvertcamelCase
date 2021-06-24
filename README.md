# ConvertcamelCase
Convertir une chaine de caractères en CamelCase 
Le but de cet exercice était de convertir une phrase au format camelCase (première lettre en minuscule, toutes les lettres suivante de chaque mot en majuscule).

Tout d'abord, nous commençons par séparer la phrase sur les espaces pour récupérer une liste contenant chaque mot :

    phrase = "Phrase en camel case"
    phrase_split = phrase.split()

Si vous vous souvenez bien, nous pouvons utiliser la fonction split sans argument pour séparer une chaîne de caractère sur les espaces (on pourrait aussi faire split(" ") pour splitter explicitement sur les espaces mais du coup c'est un peu rébarbatif et inutile).

Dans un mot en camelCase, le premier mot est en minuscule, il faut donc récupérer ce premier mot et le convertir en minuscule :

    resultat = [phrase_split.pop(0).lower()]

Ci-dessus, nous récupérons le premier élément de la liste avec la méthode pop. Cette méthode, récupère l'élément indiqué par l'indice entre parenthèse et enlève cet élément de la liste. Cela nous assure que le premier mot ne sera plus dans la liste "phrase_split" après l'opération.

Nous convertissons ensuite ce premier élément en minuscule avec la méthode lower.

Pour terminer, nous mettons ce résultat dans une liste grâce aux crochets.

La variable "resultat" contient donc maintenant le premier mot de la variable "phrase" en minuscule.

Ensuite, nous utilisons une boucle for pour passer à travers chaque mot restant dans la liste et les ajouter à la liste "resultat" avec la première lettre en majuscule grâce à la méthode capitalize :

    for mot in phrase_split:
        resultat.append(mot.capitalize())

À ce stade, nous avons donc une liste qui contient le premier mot de la phrase en minuscule et tous les autres mots, commençant par une majuscule.

Il ne reste donc plus qu'à joindre tous ces éléments ensemble grâce à la fonction join :
