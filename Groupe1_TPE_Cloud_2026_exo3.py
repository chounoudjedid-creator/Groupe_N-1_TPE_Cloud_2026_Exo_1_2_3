import tkinter as tk
from tkinter import ttk, messagebox
import re
from datetime import datetime

def valider_date(date_str):
    """Valide si une date au format AAAA-MM-JJ est valide"""
    if not re.match(r'^\d{4}-\d{2}-\d{2}$', date_str):
        return False, "Format incorrect. Utilisez AAAA-MM-JJ (ex: 2024-12-25)"
    
    try:
        annee, mois, jour = date_str.split('-')
        annee = int(annee)
        mois = int(mois)
        jour = int(jour)
        
        # Validation basique
        if mois < 1 or mois > 12:
            return False, "Mois invalide. Doit être entre 01 et 12"
        
        if jour < 1 or jour > 31:
            return False, "Jour invalide. Doit être entre 01 et 31"
        
        # Validation plus précise avec datetime
        datetime.strptime(date_str, '%Y-%m-%d')
        return True, "Date valide"
        
    except ValueError as e:
        if "day is out of range" in str(e):
            return False, f"Jour invalide pour le mois {mois:02d}"
        elif "month must be in" in str(e):
            return False, "Mois invalide"
        else:
            return False, f"Date invalide: {str(e)}"

def convertir_date():
    """Convertit la date du format AAAA-MM-JJ vers JJ/MM/AAAA"""
    date_entree = entry_date.get().strip()
    
    if not date_entree:
        messagebox.showwarning("Champ vide", "Veuillez entrer une date")
        return
    
    # Valider la date
    est_valide, message = valider_date(date_entree)
    
    if not est_valide:
        messagebox.showerror("Date invalide", message)
        # Mettre en évidence l'erreur
        entry_date.config(foreground="red")
        label_statut.config(text="❌ Date invalide", foreground="red")
        return
    
    # Date valide, on peut convertir
    try:
        annee, mois, jour = date_entree.split('-')
        date_convertie = f"{jour}/{mois}/{annee}"
        
        # Afficher le résultat
        text_resultat.delete("1.0", tk.END)
        resultat = f"📅 CONVERSION RÉUSSIE\n"
        resultat += "=" * 40 + "\n\n"
        resultat += f"Date originale :  {date_entree}\n"
        resultat += f"Date convertie :  {date_convertie}\n\n"
        resultat += "Détails :\n"
        resultat += f"  • Jour   : {jour}\n"
        resultat += f"  • Mois   : {mois}\n"
        resultat += f"  • Année  : {annee}\n\n"
        
        # Ajouter des informations supplémentaires
        date_obj = datetime.strptime(date_entree, '%Y-%m-%d')
        jours_semaine = ["Lundi", "Mardi", "Mercredi", "Jeudi", "Vendredi", "Samedi", "Dimanche"]
        mois_noms = ["Janvier", "Février", "Mars", "Avril", "Mai", "Juin", 
                    "Juillet", "Août", "Septembre", "Octobre", "Novembre", "Décembre"]
        
        resultat += f"Format long : {jours_semaine[date_obj.weekday()]} {jour} {mois_noms[int(mois)-1]} {annee}"
        
        text_resultat.insert("1.0", resultat)
        
        # Afficher aussi dans le label
        label_resultat.config(text=f"Résultat : {date_convertie}", foreground="green")
        
        # Mettre à jour le statut
        entry_date.config(foreground="green")
        label_statut.config(text="✅ Date valide", foreground="green")
        
        # Ajouter à l'historique
        ajouter_historique(date_entree, date_convertie)
        
        # Animation de succès
        animer_succes()
        
    except Exception as e:
        messagebox.showerror("Erreur", f"Erreur lors de la conversion: {str(e)}")

def ajouter_historique(date_orig, date_conv):
    """Ajoute une conversion à l'historique"""
    historique = f"{date_orig} → {date_conv}"
    
    # Limiter l'historique à 10 entrées
    liste_historique = list(listbox_historique.get(0, tk.END))
    liste_historique.insert(0, historique)
    
    if len(liste_historique) > 10:
        liste_historique = liste_historique[:10]
    
    # Mettre à jour la listbox
    listbox_historique.delete(0, tk.END)
    for item in liste_historique:
        listbox_historique.insert(tk.END, item)

def animer_succes():
    """Animation visuelle pour une conversion réussie"""
    bouton_convertir.config(bg="#4CAF50", fg="white")
    fenetre.after(300, lambda: bouton_convertir.config(bg="#2196F3", fg="white"))

def effacer_champs():
    """Efface tous les champs"""
    entry_date.delete(0, tk.END)
    text_resultat.delete("1.0", tk.END)
    label_resultat.config(text="Résultat : ", foreground="black")
    label_statut.config(text="En attente...", foreground="gray")
    entry_date.config(foreground="black")
    entry_date.focus_set()

def inserer_date_actuelle():
    """Insère la date actuelle"""
    aujourdhui = datetime.now().strftime("%Y-%m-%d")
    entry_date.delete(0, tk.END)
    entry_date.insert(0, aujourdhui)
    entry_date.config(foreground="black")

def inserer_exemple():
    """Insère un exemple de date"""
    exemple = "2024-12-25"
    entry_date.delete(0, tk.END)
    entry_date.insert(0, exemple)
    entry_date.config(foreground="black")

def formater_auto(event):
    """Formate automatiquement pendant la saisie"""
    texte = entry_date.get()
    
    # Supprimer tout sauf les chiffres
    chiffres = re.sub(r'[^\d]', '', texte)
    
    # Limiter à 8 chiffres (AAAAMMJJ)
    if len(chiffres) > 8:
        chiffres = chiffres[:8]
    
    # Formater au fur et à mesure
    if len(chiffres) >= 4:
        formatted = chiffres[:4] + "-"
        if len(chiffres) >= 6:
            formatted += chiffres[4:6] + "-"
            if len(chiffres) >= 8:
                formatted += chiffres[6:8]
            else:
                formatted += chiffres[6:]
        else:
            formatted += chiffres[4:]
    else:
        formatted = chiffres
    
    # Mettre à jour si différent
    if formatted != texte:
        entry_date.delete(0, tk.END)
        entry_date.insert(0, formatted)
    
    # Valider en temps réel
    if len(chiffres) == 8:
        valider_temps_reel()

def valider_temps_reel():
    """Validation en temps réel"""
    date_entree = entry_date.get().strip()
    
    if len(date_entree) == 10:  # Format complet
        est_valide, message = valider_date(date_entree)
        
        if est_valide:
            label_statut.config(text="✅ Format valide", foreground="green")
            entry_date.config(foreground="green")
        else:
            label_statut.config(text="❌ Format invalide", foreground="red")
            entry_date.config(foreground="red")

def on_enter(event):
    """Effet de survol pour les boutons"""
    event.widget.config(bg="#1976D2")

def on_leave(event):
    """Effet quand la souris quitte un bouton"""
    if event.widget == bouton_convertir:
        event.widget.config(bg="#2196F3")
    elif event.widget == bouton_effacer:
        event.widget.config(bg="#f44336")
    elif event.widget in [bouton_aujourdhui, bouton_exemple]:
        event.widget.config(bg="#9C27B0")

# Création de la fenêtre principale
fenetre = tk.Tk()
fenetre.title("Convertisseur de Dates")
fenetre.geometry("750x650")
fenetre.configure(bg="#f5f5f5")
fenetre.resizable(False, False)

# Style
style = ttk.Style()
style.theme_use('clam')

# Titre principal
frame_titre = tk.Frame(fenetre, bg="#2196F3", height=100)
frame_titre.pack(fill=tk.X)
frame_titre.pack_propagate(False)

label_titre = tk.Label(
    frame_titre, 
    text="📅 CONVERTISSEUR DE DATES", 
    font=("Helvetica", 24, "bold"),
    bg="#2196F3",
    fg="white"
)
label_titre.pack(expand=True, pady=(20, 0))

label_sous_titre = tk.Label(
    frame_titre,
    text="Convertit les dates du format AAAA-MM-JJ vers JJ/MM/AAAA",
    font=("Helvetica", 11),
    bg="#2196F3",
    fg="#C5CAE9"
)
label_sous_titre.pack(expand=True, pady=(0, 20))

# Conteneur principal
conteneur = tk.Frame(fenetre, bg="#f5f5f5", padx=30, pady=20)
conteneur.pack(fill=tk.BOTH, expand=True)

# Section d'entrée
frame_entree = tk.LabelFrame(
    conteneur, 
    text=" Entrée de la date ", 
    font=("Helvetica", 12, "bold"),
    bg="white",
    fg="#333333",
    relief=tk.GROOVE,
    borderwidth=2
)
frame_entree.pack(fill=tk.X, pady=(0, 15))

# Instructions
label_instructions = tk.Label(
    frame_entree,
    text="Entrez une date au format AAAA-MM-JJ (ex: 2024-12-25) :",
    font=("Helvetica", 10),
    bg="white",
    fg="#555555",
    anchor="w"
)
label_instructions.pack(fill=tk.X, padx=15, pady=(15, 5))

# Champ de saisie avec validation
frame_saisie = tk.Frame(frame_entree, bg="white")
frame_saisie.pack(fill=tk.X, padx=15, pady=(0, 10))

label_format = tk.Label(
    frame_saisie,
    text="AAAA-MM-JJ",
    font=("Helvetica", 10, "italic"),
    bg="white",
    fg="#777777"
)
label_format.pack(side=tk.LEFT, pady=5)

entry_date = tk.Entry(
    frame_saisie,
    font=("Helvetica", 14),
    bg="#FAFAFA",
    fg="#333333",
    relief=tk.SOLID,
    borderwidth=2,
    width=20,
    justify="center"
)
entry_date.pack(side=tk.LEFT, padx=(10, 0))
entry_date.bind("<KeyRelease>", formater_auto)
entry_date.bind("<Return>", lambda e: convertir_date())

# Indicateur de statut
label_statut = tk.Label(
    frame_saisie,
    text="En attente...",
    font=("Helvetica", 10),
    bg="white",
    fg="gray"
)
label_statut.pack(side=tk.LEFT, padx=(15, 0))

# Boutons rapides
frame_boutons_rapides = tk.Frame(frame_entree, bg="white")
frame_boutons_rapides.pack(fill=tk.X, padx=15, pady=(0, 15))

bouton_aujourdhui = tk.Button(
    frame_boutons_rapides,
    text="Date du jour",
    font=("Helvetica", 10),
    bg="#9C27B0",
    fg="white",
    activebackground="#7B1FA2",
    activeforeground="white",
    relief=tk.RAISED,
    borderwidth=2,
    cursor="hand2",
    command=inserer_date_actuelle
)
bouton_aujourdhui.pack(side=tk.LEFT, padx=(0, 10))
bouton_aujourdhui.bind("<Enter>", on_enter)
bouton_aujourdhui.bind("<Leave>", on_leave)

bouton_exemple = tk.Button(
    frame_boutons_rapides,
    text="Exemple (Noël 2025)",
    font=("Helvetica", 10),
    bg="#9C27B0",
    fg="white",
    activebackground="#7B1FA2",
    activeforeground="white",
    relief=tk.RAISED,
    borderwidth=2,
    cursor="hand2",
    command=inserer_exemple
)
bouton_exemple.pack(side=tk.LEFT)
bouton_exemple.bind("<Enter>", on_enter)
bouton_exemple.bind("<Leave>", on_leave)

# Section de conversion
frame_conversion = tk.Frame(conteneur, bg="#f5f5f5")
frame_conversion.pack(fill=tk.X, pady=(10, 15))

# Bouton de conversion principal
bouton_convertir = tk.Button(
    frame_conversion,
    text="CONVERTIR LA DATE",
    font=("Helvetica", 12, "bold"),
    bg="#2196F3",
    fg="white",
    activebackground="#1976D2",
    activeforeground="white",
    relief=tk.RAISED,
    borderwidth=3,
    cursor="hand2",
    padx=40,
    pady=12,
    command=convertir_date
)
bouton_convertir.pack()
bouton_convertir.bind("<Enter>", on_enter)
bouton_convertir.bind("<Leave>", on_leave)

# Label pour afficher rapidement le résultat
label_resultat = tk.Label(
    frame_conversion,
    text="Résultat : ",
    font=("Helvetica", 12),
    bg="#f5f5f5",
    fg="black"
)
label_resultat.pack(pady=(10, 0))

# Section des résultats
frame_resultats = tk.LabelFrame(
    conteneur, 
    text=" Détails de la conversion ", 
    font=("Helvetica", 12, "bold"),
    bg="white",
    fg="#333333",
    relief=tk.GROOVE,
    borderwidth=2
)
frame_resultats.pack(fill=tk.BOTH, expand=True, pady=(0, 15))

# Zone de texte pour les résultats détaillés
text_resultat = tk.Text(
    frame_resultats,
    font=("Consolas", 11),
    bg="#FAFAFA",
    fg="#333333",
    relief=tk.SOLID,
    borderwidth=1,
    wrap=tk.WORD,
    height=8
)
text_resultat.pack(fill=tk.BOTH, expand=True, padx=15, pady=15)

# Ajouter une barre de défilement
scrollbar = tk.Scrollbar(text_resultat)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
text_resultat.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=text_resultat.yview)

# Section historique
frame_historique = tk.LabelFrame(
    conteneur,
    text=" Historique des conversions (10 max) ",
    font=("Helvetica", 10, "bold"),
    bg="white",
    fg="#666666",
    relief=tk.GROOVE,
    borderwidth=1
)
frame_historique.pack(fill=tk.X, pady=(0, 15))

# Listbox pour l'historique
listbox_historique = tk.Listbox(
    frame_historique,
    font=("Consolas", 9),
    bg="#F8F8F8",
    fg="#333333",
    relief=tk.SOLID,
    borderwidth=1,
    height=4
)
listbox_historique.pack(fill=tk.X, padx=10, pady=10)

# Bouton effacer
frame_boutons_bas = tk.Frame(conteneur, bg="#f5f5f5")
frame_boutons_bas.pack(fill=tk.X)

bouton_effacer = tk.Button(
    frame_boutons_bas,
    text="TOUT EFFACER",
    font=("Helvetica", 10, "bold"),
    bg="#f44336",
    fg="white",
    activebackground="#D32F2F",
    activeforeground="white",
    relief=tk.RAISED,
    borderwidth=2,
    cursor="hand2",
    padx=20,
    pady=8,
    command=effacer_champs
)
bouton_effacer.pack()
bouton_effacer.bind("<Enter>", on_enter)
bouton_effacer.bind("<Leave>", on_leave)

# Guide de format
frame_guide = tk.Frame(fenetre, bg="#E8F5E9", height=40)
frame_guide.pack(fill=tk.X, side=tk.BOTTOM)
frame_guide.pack_propagate(False)

label_guide = tk.Label(
    frame_guide,
    text="Format d'entrée: AAAA-MM-JJ | Format de sortie: JJ/MM/AAAA | Exemple: 2024-12-25 → 25/12/2024",
    font=("Helvetica", 9),
    bg="#E8F5E9",
    fg="#2E7D32"
)
label_guide.pack(expand=True)

# Insérer un exemple par défaut
inserer_exemple()

# Focus sur le champ de saisie
entry_date.focus_set()

# Lancer l'application
fenetre.mainloop()