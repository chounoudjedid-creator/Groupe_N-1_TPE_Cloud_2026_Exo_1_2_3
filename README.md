# Groupe_N_1_TPE_Cloud_2026_Exo_1_2_3





🖥️ Projet de Travaux Pratiques (TPE) - Cloud 2026

Groupe 1

    

Ce projet contient trois applications Python développées avec Tkinter, illustrant :

Manipulation de structures de données

Traitement de chaînes de caractères

Validation et conversion de formats de dates



📌 Sommaire

1. Membres du Groupe


2. Méthodologie de Travail


3. Explications Techniques des Exercices

Exercice 1 : Détecteur de Palindromes

Exercice 2 : Détecteur de Doublons

Exercice 3 : Convertisseur de Date



4. Lancement des Exercices

Sur PC

Sur Android avec Pydroid



5. Fichiers du Projet


6. Captures d’Écran


7. Conclusion




👥 Membres du Groupe (Ordre alphabétique)

Nom	Matricule

BICHARA ABAKAR HANGATA	23B472FS

DJERABE OSE	23A751FS

FALMATA HAROUN KAMBA	23A868FS

HISSEIN YAYA BOUNA	23A054FS

MAHAMAT TAHIR ISSA	23A930FS



🛠️ Méthodologie de Travail

Le groupe a suivi une approche structurée :

1. Analyse des besoins

Compréhension des trois exercices : palindromes, doublons, dates.

Définition des attentes pour l’interface Tkinter.



2. Développement collaboratif

Répartition des tâches entre les membres.

Fusion et uniformisation du code pour un rendu graphique cohérent et esthétique.



3. Tests et validation

Gestion des erreurs avec try/except.

Vérification du format des entrées avec re et datetime.

Tests croisés pour fiabilité et robustesse.





---

🧠 Explications Techniques des Exercices

Exercice 1 : Détecteur de Palindromes

Problème : Identifier les nombres identiques lus de gauche à droite et de droite à gauche.

Solution :

Extraction des nombres : re pour filtrer uniquement les chiffres.

Vérification palindrome :

if str(nb) == str(nb)[::-1]:
    palindromes.append(nb)

Interface Tkinter : Affichage dynamique avec compteur et historique.



---

Exercice 2 : Détecteur de Doublons (Sans set)

Problème : Identifier les éléments répétés dans une liste.

Solution :

Parcours manuel :

Listes elements_vus et doublons.

Si élément déjà dans elements_vus mais pas dans doublons → ajout à doublons.


Interface Tkinter : Affichage clair du nombre d’occurrences et mise en valeur des doublons.



---

Exercice 3 : Convertisseur de Format de Date

Problème : Valider AAAA-MM-JJ et convertir en JJ/MM/AAAA.

Solution :

Validation : Regex + datetime.strptime pour rejeter les dates invalides.

Conversion :

jj, mm, aaaa = date.split('-')[2], date.split('-')[1], date.split('-')[0]
formatted = f"{jj}/{mm}/{aaaa}"

Fonctionnalités avancées :

Calcul automatique du jour de la semaine

Nom du mois en français

Saisie automatique de la date actuelle


Interface Tkinter : Résultat clair, possibilité de copier ou exporter.



---

🚀 Lancement des Exercices

Sur PC

python Groupe1_TPE_Cloud_2026_exo1.py
python Groupe1_TPE_Cloud_2026_exo2.py
python Groupe1_TPE_Cloud_2026_exo3.py

Sur Android avec Pydroid

1. Installer Pydroid 3 depuis le Play Store.


2. Copier les fichiers .py dans un dossier accessible.


3. Ouvrir Pydroid → sélectionner le fichier → appuyer sur Run.



> Tkinter fonctionne mais certaines animations ou pop-ups peuvent varier légèrement.




---

📂 Fichiers du Projet

Fichier	Description

Groupe1_TPE_Cloud_2026_exo1.py	Détecteur de palindromes numériques
Groupe1_TPE_Cloud_2026_exo2.py	Détecteur de doublons
Groupe1_TPE_Cloud_2026_exo3.py	Convertisseur de format de date
/screenshots/	Dossier contenant toutes les captures d’écran des applications



---

🖼️ Captures d’Écran


**Exercice 1 : Détecteur de Palindromes**  
![Palindromes](./screenshots/exo1.png)

**Exercice 2 : Détecteur de Doublons**  
![Doublons](./screenshots/exo2.png)

**Exercice 3 : Convertisseur de Date**  
![Date](./screenshots/exo3.png)


📌 Conclusion

Application pratique des concepts Python et Tkinter.

Renforcement des compétences en validation et manipulation de données.

Travail collaboratif structuré et efficace, avec répartition claire des tâches.
