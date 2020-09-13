# Jours 09-12 Construire des API avec Api Star (0.5.41)

**Important** : au moment de l'enregistrement, la dernière version de `apistar` était la `0.5.41`, qui vous permettait de construire des API complètes. 

Mais si vous regardez la [documentation du projet] (https://docs.apistar.com) aujourd'hui, vous verrez la note suivante :

> Avec la version 0.6 et les suivantes, le projet API Star se concentre sur une suite d'outils d'API à la fois cadres et anorexiques. Il est prévu de développer cette fonctionnalité de manière à ce qu'elle puisse être utilisée soit comme un outil autonome, soit avec un large éventail de cadres. La branche 0.5 reste disponible sur GitHub, et peut être installée depuis PyPI avec `pip install apistar==0.5.41`.

Pour cette raison et afin que le projet de démonstration fonctionne, nous l'avons épinglé à la version `0.5.41`.

---

## Jour 1-2 : Regardez les leçons en vidéo

La première moitié de ce bloc de 4 jours consiste à regarder les vidéos et à étudier API Star. Envisagez de télécharger et d'essayer les échantillons de code développés pendant le cours.

## Jour 3 : Créez votre propre API

Maintenant que vous avez vu les vidéos de ce chapitre, vous êtes prêt à construire une API en utilisant API Star !

Pour ce jour, vous obtiendrez un ensemble de données de [Mockaroo] (https://mockaroo.com/) ou de toute autre ressource et vous le chargerez dans une structure de données sensible (dans la démo, j'ai utilisé une "liste" de "dict").

Les données sont partout, mais si vous n'avez pas d'inspiration, vous pouvez peut-être utiliser ce [jeu de données Marvel] (https://raw.githubusercontent.com/pybites/marvel_challenge/master/marvel-wikia-data.csv) que nous avons utilisé pour l'un de nos défis de code. Si vous ne savez pas comment analyser le CSV, pas de problème : le même repo [a un code pour cela](https://github.com/pybites/marvel_challenge/blob/solution/marvel.py).

Ensuite, créez un environnement virtuel, activez-le et installez apistar==0.5.41 comme indiqué dans les vidéos (bien sûr, vous pouvez aussi utiliser `pipenv` ou `Anaconda`).

Ensuite, commencez à construire votre API en utilisant le squelette de ma démo. Essayez d'implémenter le point final `GET` dès aujourd'hui (à la fois tous les éléments et un seul élément).

## Jour 4 : Développer (et tester) l'API

Ensuite, continuez votre API en mettant en œuvre les autres opérations du CRUD : POST, PUT (mise à jour) et DELETE (**note** les requêtes PUT nécessitent une barre oblique !). Assurez-vous d'ajouter les `404`s (données non présentes) le cas échéant.

Vous pouvez aussi ajouter des validations personnalisées (comme l'exemple du fabricant "enum" dans la leçon). Voir la [API Star docs] (https://docs.apistar.com/type-system/).

Installez [Postman](https://www.getpostman.com/) et exécutez les différentes méthodes sur les différents terminaux, est-ce qu'elles renvoient toutes les données et les codes d'état attendus ?

S'il vous reste du temps, essayez d'écrire quelques tests pour automatiser l'étape précédente. Je vous recommande d'utiliser "pytest" mais ce n'est pas obligatoire. Vous voudrez probablement utiliser [Api Star's TestClient] (https://github.com/encode/apistar/blob/version-0.5.x/docs/api-guide/testing.md) pour plus de commodité (*note* cela fonctionne pour la version que nous utilisons dans cette leçon = 0.5, [à partir de 0.6 c'est obsolète] (https://docs.apistar.com/#where-did-the-server-go)).

Bonne chance et n'oubliez pas : l'apprentissage est dans la pratique.

### Il est temps de partager ce que vous avez accompli !

N'oubliez pas de partager votre travail des deux derniers jours sur Twitter ou Facebook. Utilisez le hashtag **#100JoursFullstackWebPython**. 

Pensez à inclure [@martialobug](https://twitter.com/martialobug) dans vos tweets.

*Voir une erreur dans ces instructions ? Veuillez [soumettre un nouveau numéro](https://github.com/martialodev/100JoursFullstackWebPython/issues).*
