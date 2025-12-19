import tkinter as tk
from tkinter import messagebox

def trouver_doublons(liste):
    """Fonction qui détecte les éléments en double sans utiliser de sets"""
    doublons = []
    elements_vus = []
    
    for element in liste:
        # Vérifier si l'élément a déjà été vu
        deja_vu = False
        for vu in elements_vus:
            if vu == element:
                deja_vu = True
                break
        
        if deja_vu:
            # Vérifier si ce doublon n'est pas déjà dans la liste des doublons
            deja_doublon = False
            for d in doublons:
                if d == element:
                    deja_doublon = True
                    break
            
            if not deja_doublon:
                doublons.append(element)
        else:
            elements_vus.append(element)
    
    return doublons, elements_vus

def analyser_liste():
    """Fonction principale pour analyser la liste"""
    # Récupérer le texte
    texte = zone_texte.get("1.0", tk.END).strip()
    
    if not texte:
        messagebox.showwarning("Erreur", "Veuillez entrer des éléments")
        return
    
    # Séparer les éléments
    if "," in texte:
        elements = [e.strip() for e in texte.split(",") if e.strip()]
    else:
        elements = [e.strip() for e in texte.split() if e.strip()]
    
    if not elements:
        messagebox.showwarning("Erreur", "Aucun élément valide trouvé")
        return
    
    # Trouver les doublons
    doublons, uniques = trouver_doublons(elements)
    
    # Afficher les résultats
    resultat = f"ANALYSE TERMINÉE\n"
    resultat += "="*40 + "\n"
    resultat += f"Éléments analysés : {len(elements)}\n"
    resultat += f"Éléments uniques : {len(uniques)}\n"
    resultat += f"Doublons trouvés : {len(doublons)}\n\n"
    
    if doublons:
        resultat += "LISTE DES DOUBLONS :\n"
        resultat += "-"*30 + "\n"
        for i, d in enumerate(doublons, 1):
            # Compter les occurrences
            compte = 0
            for e in elements:
                if e == d:
                    compte += 1
            resultat += f"{i}. '{d}' apparaît {compte} fois\n"
        
        resultat += "\nÉLÉMENTS UNIQUES :\n"
        resultat += "-"*30 + "\n"
        resultat += ", ".join(uniques) + "\n"
    else:
        resultat += "✅ AUCUN DOUBLON TROUVÉ !\n"
        resultat += "Tous les éléments sont uniques.\n\n"
        resultat += "ÉLÉMENTS :\n"
        resultat += "-"*30 + "\n"
        resultat += ", ".join(elements) + "\n"
    
    # Mettre à jour l'affichage
    zone_resultat.config(state="normal")
    zone_resultat.delete("1.0", tk.END)
    zone_resultat.insert("1.0", resultat)
    zone_resultat.config(state="disabled")
    
    # Mettre à jour le compteur
    compteur.config(text=f"Doublons: {len(doublons)}")
    
    # Changer la couleur du compteur
    if len(doublons) == 0:
        compteur.config(bg="green", fg="white")
    else:
        compteur.config(bg="red", fg="white")

def effacer_tout():
    """Efface tous les champs"""
    zone_texte.delete("1.0", tk.END)
    zone_resultat.config(state="normal")
    zone_resultat.delete("1.0", tk.END)
    zone_resultat.config(state="disabled")
    compteur.config(text="Doublons: 0", bg="gray", fg="white")

def charger_exemple1():
    """Charge un exemple de fruits avec doublons"""
    exemple = "pomme, banane, orange, pomme, raisin, banane, kiwi, orange, pomme, fraise"
    zone_texte.delete("1.0", tk.END)
    zone_texte.insert("1.0", exemple)

def charger_exemple2():
    """Charge un exemple de nombres avec doublons"""
    exemple = "1, 5, 2, 5, 3, 1, 4, 5, 2, 6, 7, 8, 9, 10, 1"
    zone_texte.delete("1.0", tk.END)
    zone_texte.insert("1.0", exemple)

# Création de la fenêtre principale
fenetre = tk.Tk()
fenetre.title("Détecteur de Doublons")
fenetre.geometry("700x600")
fenetre.configure(bg="#f0f0f0")

# Titre
titre = tk.Label(fenetre, 
                 text="🔍 DÉTECTEUR DE DOUBLONS", 
                 font=("Arial", 18, "bold"),
                 bg="#2c3e50",
                 fg="white",
                 pady=10)
titre.pack(fill=tk.X)

sous_titre = tk.Label(fenetre,
                      text="Détecte les éléments en double sans utiliser de collections ni de sets",
                      font=("Arial", 10),
                      bg="#34495e",
                      fg="white")
sous_titre.pack(fill=tk.X, pady=(0, 20))

# Conteneur principal
conteneur = tk.Frame(fenetre, bg="#f0f0f0", padx=20, pady=10)
conteneur.pack(fill=tk.BOTH, expand=True)

# Section d'entrée
frame_entree = tk.LabelFrame(conteneur, 
                            text=" Entrez vos éléments ",
                            font=("Arial", 12, "bold"),
                            bg="white",
                            padx=10,
                            pady=10)
frame_entree.pack(fill=tk.X, pady=(0, 10))

# Label d'instructions
label_instructions = tk.Label(frame_entree,
                             text="Séparez les éléments par des virgules :",
                             font=("Arial", 10),
                             bg="white",
                             anchor="w")
label_instructions.pack(fill=tk.X)

# Zone de texte pour l'entrée
zone_texte = tk.Text(frame_entree,
                    height=4,
                    font=("Arial", 11),
                    bg="#f8f9fa",
                    relief=tk.SOLID,
                    borderwidth=1)
zone_texte.pack(fill=tk.X, pady=5)

# Boutons d'exemple
frame_boutons_exemple = tk.Frame(frame_entree, bg="white")
frame_boutons_exemple.pack(fill=tk.X, pady=(5, 0))

btn_exemple1 = tk.Button(frame_boutons_exemple,
                        text="Exemple Fruits",
                        command=charger_exemple1,
                        bg="#3498db",
                        fg="white",
                        font=("Arial", 9),
                        padx=10,
                        pady=5)
btn_exemple1.pack(side=tk.LEFT, padx=(0, 10))

btn_exemple2 = tk.Button(frame_boutons_exemple,
                        text="Exemple Nombres",
                        command=charger_exemple2,
                        bg="#9b59b6",
                        fg="white",
                        font=("Arial", 9),
                        padx=10,
                        pady=5)
btn_exemple2.pack(side=tk.LEFT)

# Bouton d'analyse
frame_analyse = tk.Frame(conteneur, bg="#f0f0f0")
frame_analyse.pack(fill=tk.X, pady=(10, 10))

btn_analyser = tk.Button(frame_analyse,
                        text="ANALYSER LA LISTE",
                        command=analyser_liste,
                        bg="#27ae60",
                        fg="white",
                        font=("Arial", 12, "bold"),
                        padx=30,
                        pady=10,
                        cursor="hand2")
btn_analyser.pack()

# Compteur de doublons
compteur = tk.Label(frame_analyse,
                   text="Doublons: 0",
                   font=("Arial", 12, "bold"),
                   bg="gray",
                   fg="white",
                   padx=20,
                   pady=5)
compteur.pack(pady=(10, 0))

# Section des résultats
frame_resultats = tk.LabelFrame(conteneur,
                               text=" Résultats ",
                               font=("Arial", 12, "bold"),
                               bg="white",
                               padx=10,
                               pady=10)
frame_resultats.pack(fill=tk.BOTH, expand=True, pady=(0, 10))

# Zone de texte pour les résultats
zone_resultat = tk.Text(frame_resultats,
                       height=12,
                       font=("Consolas", 10),
                       bg="#f8f9fa",
                       relief=tk.SOLID,
                       borderwidth=1,
                       state="disabled")
zone_resultat.pack(fill=tk.BOTH, expand=True)

# Ajouter une scrollbar
scrollbar = tk.Scrollbar(zone_resultat)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
zone_resultat.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=zone_resultat.yview)

# Bouton effacer
frame_boutons = tk.Frame(conteneur, bg="#f0f0f0")
frame_boutons.pack(fill=tk.X)

btn_effacer = tk.Button(frame_boutons,
                       text="TOUT EFFACER",
                       command=effacer_tout,
                       bg="#e74c3c",
                       fg="white",
                       font=("Arial", 10),
                       padx=20,
                       pady=5)
btn_effacer.pack()

# Informations
frame_info = tk.Frame(fenetre, bg="#ecf0f1", pady=5)
frame_info.pack(fill=tk.X, side=tk.BOTTOM)

info = tk.Label(frame_info,
               text="Algorithme : Simple parcours avec liste de contrôle • Sans collections ni sets",
               font=("Arial", 8),
               bg="#ecf0f1",
               fg="#7f8c8d")
info.pack()

# Charger un exemple par défaut
charger_exemple1()

# Lancer l'application
fenetre.mainloop()