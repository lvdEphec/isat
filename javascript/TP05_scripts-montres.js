
// Brouillon de quelques scripts montrés durant le TP de rappel Javascript (mars 2018)

-------------------------------------------------------------------

// Rappel parcourir array

heros = ["hulk", "musclor", "batman"]

// classique, ancien, fonctionne bien
for (let i = 0; i < heros.length; i++) {
    console.log(i);
}

for (let i = 0; i < heros.length; i++) {
    console.log(heros[i]);
}

for (let i in heros) {
 console.log(i);
}

// plus moderne, pratique si correspond au besoin, gaffe compatibilité
for (let e of heros) {
 console.log(e);
}

// ça fonctionne
Object.keys(heros)

// pas de sens mais fonctionne
Object.values(heros)

--------------------------------------------------------

// Rappels parcourir object

// clef des objets considérés comme string mais " pas nécessaires. Par contre pour les valeurs, variables doivent exister ou alors valeurs brutes
repas = {entree: tapas, plat: tacos, dessert: churros, boisson: tequila};

repas = {entree: "tapas", plat: "tacos", dessert: "churros", boisson: "tequila"};

for (let k in repas) {
 console.log(k);
}

// KO
for (let v of repas) {
 console.log(k);
}

for (let k in repas) {
 console.log(repas[k]);
}

// undefined, ok, se méfier
repas.k

// ko, pas d'attribut possible à undefined, au moins ça plante. A l'exame on s'attend à que ça ne plante pas (au pire mis en commentaire avec explications)
repas.k.j

repas.plat
repas['plat']
repas[plat]

Object.keys(repas)

Object.values(repas)

for (let v of Object.values(repas)) {
 console.log(v);
}

// similaire
for (let k in repas) {
 console.log(repas[k]);
}

// demander : à votre avis, sous quelle forme est renvoyée clef/valeur?
Object.entries(repas)

for (let c of Object.entries(repas)) {
    console.log(c[0]);
}

for (let c of Object.entries(repas)) {    
   console.log(c[0] + " : " + c[1]);
}

// resultat similaire
for (let k in repas) {
 console.log(k + " : " + repas[k]);
}

--------------------------------------------------------

// Nouveauté fonctions flêchées

// fonctions flêchées pratique pour décrire un comportement
// souvent utilisées de manière similaire aux fonctions anonymes
// (attention, subtilités : pas de this, arguments, new...)
// Pas mal utilisé maintenant. Habituel aussi en programmation fonderne d'utiliser des fonctions pour en générer d'autres, d'en envoyer en paramètre, lamdba, etc...
x => x + 1

(x => x + 1)(5)

(function (x) { return x + 1; })(8)

heros = ["hulk", "musclor", "batman"]

superHeros = heros.map(x => "super " + x)

// map ne modifie pas
heros

// avec fonction anonyme
superHeros = heros.map(function(x) { return "super " + x})

//avec fonction nommée
function superiser(x) { return "super " + x}

superiser("mario bross")

superHeros = heros.map(superiser)

superiser

superiser()

----------------------------------

// Rappel tri sur string

// trier string en se basant sur dictionnaire de l'utilisateur peut être pratique. Se méfier si ordre toujours identique oligatoire.
"heros".localeCompare("tata")
"heros".localeCompare("heros")
"heros".localeCompare("héros")
 
heros.sort((x,y) => x.localeCompare(y))
heros.sort((x,y) => y.localeCompare(x))

-----------------------------------------------------------

// Rappel : concept d'index 

repas = {entree: "tapas", plat: "tacos", dessert: "churros", boisson: "tequila"};

// principe d'index permet d'utiliser les ressources pour trier une seule fois, puis après se baser sur l'index stocké pour parcourir dans l'ordre désiré rapidement.
// concept utilisé en bases de données, peut permettre de réduire durée requêtes (mais nécessitent d'être stockés et mis à jour) : 
// montrer exemple au tableau de tris différent et ordre de la clef . Ex : id, nom, age et trier sur nom puis sur age

index1 = Object.keys(repas).sort((x, y) => x.localeCompare(y))

for (let k of index1) {
    console.log( k + " : " + repas[k]);
}

// un peu plus avancé... mais devrait être ok.
// montrer au tableau évolution

index2 = Object.entries(repas)
               .sort((x, y) => x[1].localeCompare(y[1]))
               .map(x => x[0]);
			   
for (let k of index2) {
    console.log( k + " : " + repas[k]);
}

// on peut choisir l'ordre en fonction de l'index sans devoir trier à nouveau.
for (let k of index1) {
    console.log( k + " : " + repas[k]);
}

---------------------------------------------------------------

// construction  de string

// manquait formatage facile en JS, maintenant ok
// dans ${} est interprété (variable, calcul, fonction...)

for (let k of index2) {
    console.log( `Votre choix pour ${k} est ${repas[k]} !`);
}

// attention, bien utiliser accent grave. Pourquoi nouveau? Ne pas poser de problèmes aux anciens programmes qui utiliseraient ${} en string par exemple
for (let k in repas) {
 console.log('Votre choix pour ${k} est ${repas[k]}');
}

------------------------------------------------------------

// Accéder au contenu d'un élément html
document.getElementById(idElem).innerHTML

// ATTENTION : Accéder à la valeur d'un élément "input" html
document.getElementById(idElemInput).value

document.getElementById(idForm).nomInput.value


------------------------------------------------------------

// sélecteurs, JQuery, dev Chrome

document.getElementsByTagName('a')

document.querySelector("a")
document.querySelector(".a")
document.querySelector("#a")
document.querySelectorAll("a")
document.querySelectorAll("div a")

// affiche la version de Jquery (erreur si non installé sur le site)
$().jquery

// si installé, les affiche tous
// sinon, chrome affiche le premier : équivalent de querySelector. pratique en dev
$("a")

// dans chrome équivalent de querySelectorAll
$$("a")

// jquery est une librairie permettant d'écrire des codes plus cours et plus simpels qu'en Javascript pur
// un peu moins vrai avec les dernières évolutions de Javascript
// Certains disent que Jquery est mort, mais encore une des librairies plus utilisées, connues, risque de durer encore
// je fais partie de ceux qui préfèrent écrire du code en JS natif (Vanilla JS), cela évite de charger une librairie au début
// mais il faut reconnaitre que c'est très bien fichu, facile et eficace.
// à noter que l'on peut charger la librairie sur son serveur ou ailleurs (google, etc...)
// parler des versions minimales, illisibles par un humain mais plus légères
// on ne l'utilisera pas en 1ère, mais bien l'année prochaine

// pratique pour les sélections
https://learn.jquery.com/using-jquery-core/selecting-elements/

// pratique pour gérer les évènements
https://learn.jquery.com/events/event-basics/

// pratique pour des évènements
https://learn.jquery.com/effects/intro-to-effects/

// pratique pour Ajax
https://learn.jquery.com/ajax/jquery-ajax-methods/

---------------------------------------------------------

// Montrer exemple de code JS lié à l'examen précédent

-----------------------------------------------------------

//Renvoyer une fonction comme résultat... utiliser des fonction pour crééer des fonctions... garder en mémoire des variables à l'intérieur du contexte d'une fonction... 
// un peu plus avancé mais très utilisé. Exemple simple :

function preparerAddition(constante) {
  return function(x) { return x + constante;};
}

additionner5 = preparerAddition(5);

additionner5(7)

function preparerAddition(constante) {
  return x => x + constante;
}

additionner2 = preparerAddition(2)

additionner2(14)


--------------------------------------------------------------












