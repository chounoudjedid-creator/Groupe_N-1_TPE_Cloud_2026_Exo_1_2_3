import tkinter as tk
from tkinter import ttk, messagebox
import re

def est_palindrome(nombre):
    """Vérifie si un nombre est un palindrome (identique quand lu de droite à gauche)"""
    return str(nombre) == str(nombre)[::-1]

def trouver_palindromes():
    """Fonction principale qui extrait et affiche les palindromes"""
    # Récupérer l'entrée utilisateur
    entree = entry_nombres.get("1.0", tk.END).strip()
    
    if not entree:
        messagebox.showwarning("Entrée vide", "Veuillez entrer une liste de nombres.")
        return
    
    # Nettoyer et diviser l'entrée
    entree_nettoyee = re.sub(r'[^\d\s,]', '', entree)
    
    # Essayer différentes méthodes de séparation
    nombres_list = []
    if ',' in entree_nettoyee:
        nombres_list = entree_nettoyee.split(',')
    else:
        nombres_list = entree_nettoyee.split()
    
    # Filtrer les éléments vides et convertir en nombres
    nombres_valides = []
    for nb in nombres_list:
        nb = nb.strip()
        if nb:
            try:
                # Garder les nombres comme chaînes pour préserver les zéros initiaux si nécessaire
                nombres_valides.append(nb)
            except ValueError:
                pass
    
    if not nombres_valides:
        messagebox.showerror("Erreur", "Aucun nombre valide trouvé dans l'entrée.")
        return
    
    # Trouver les palindromes
    palindromes = [nb for nb in nombres_valides if est_palindrome(nb)]
    
    # Mettre à jour l'affichage des résultats
    resultat_text = f"Sur {len(nombres_valides)} nombre(s) analysé(s) :\n"
    resultat_text += f"→ {len(palindromes)} palindrome(s) trouvé(s)\n\n"
    
    if palindromes:
        resultat_text += "Palindromes trouvés :\n"
        for i, palindrome in enumerate(palindromes, 1):
            resultat_text += f"{i}. {palindrome}\n"
        
        # Exemples d'inversion pour démonstration
        resultat_text += "\nExemples d'inversion :\n"
        for i, palindrome in enumerate(palindromes[:3], 1):
            inverse = palindrome[::-1]
            resultat_text += f"{palindrome} → {inverse} {'✓' if palindrome == inverse else '✗'}\n"
    else:
        resultat_text += "Aucun palindrome trouvé dans la liste."
    
    text_resultat.delete("1.0", tk.END)
    text_resultat.insert("1.0", resultat_text)
    
    # Mettre à jour le compteur
    label_compteur.config(text=f"Palindromes: {len(palindromes)}")
    
    # Changer la couleur du bouton temporairement pour feedback visuel
    bouton_rechercher.config(bg="#4CAF50", fg="white")
    root.after(300, lambda: bouton_rechercher.config(bg="#2196F3", fg="white"))

def effacer_champs():
    """Efface tous les champs de l'interface"""
    entry_nombres.delete("1.0", tk.END)
    text_resultat.delete("1.0", tk.END)
    label_compteur.config(text="Palindromes: 0")
    entry_nombres.focus_set()

def inserer_exemple():
    """Insère un exemple de liste de nombres"""
    exemple = "121, 123, 1331, 45654, 789, 12321, 1001, 555, 1234321, 99, 10"
    entry_nombres.delete("1.0", tk.END)
    entry_nombres.insert("1.0", exemple)

def on_enter(event):
    """Effet de survol pour les boutons"""
    event.widget.config(bg="#1976D2")

def on_leave(event):
    """Effet quand la souris quitte un bouton"""
    event.widget.config(bg="#2196F3")

# Création de la fenêtre principale
root = tk.Tk()
root.title("Détecteur de Palindromes Numériques")
root.geometry("800x650")
root.resizable(True, True)
root.configure(bg="#f5f5f5")

# Style
style = ttk.Style()
style.theme_use('clam')

# Titre principal
frame_titre = tk.Frame(root, bg="#2196F3", height=100)
frame_titre.pack(fill=tk.X, pady=(0, 20))
frame_titre.pack_propagate(False)

label_titre = tk.Label(
    frame_titre, 
    text="🔍 Détecteur de Palindromes Numériques", 
    font=("Helvetica", 20, "bold"),
    bg="#2196F3",
    fg="white"
)
label_titre.pack(expand=True)

label_sous_titre = tk.Label(
    frame_titre,
    text="Un palindrome numérique reste identique quand on le lit de droite à gauche",
    font=("Helvetica", 10),
    bg="#2196F3",
    fg="#E3F2FD"
)
label_sous_titre.pack(expand=True, pady=(0, 10))

# Frame principal pour le contenu
frame_principal = tk.Frame(root, bg="#f5f5f5")
frame_principal.pack(fill=tk.BOTH, expand=True, padx=30, pady=10)

# Frame pour l'entrée
frame_entree = tk.LabelFrame(
    frame_principal, 
    text=" Entrez vos nombres ", 
    font=("Helvetica", 12, "bold"),
    bg="#ffffff",
    fg="#333333",
    relief=tk.GROOVE,
    borderwidth=2
)
frame_entree.pack(fill=tk.X, pady=(0, 15))

# Instructions
label_instructions = tk.Label(
    frame_entree,
    text="Séparez les nombres par des virgules, des espaces ou des retours à ligne :",
    font=("Helvetica", 10),
    bg="#ffffff",
    fg="#555555",
    anchor="w"
)
label_instructions.pack(fill=tk.X, padx=15, pady=(10, 5))

# Zone de texte pour l'entrée
entry_nombres = tk.Text(
    frame_entree,
    height=6,
    font=("Courier New", 11),
    bg="#FAFAFA",
    fg="#333333",
    relief=tk.SOLID,
    borderwidth=1,
    wrap=tk.WORD
)
entry_nombres.pack(fill=tk.X, padx=15, pady=(0, 10))

# Boutons d'action
frame_boutons = tk.Frame(frame_entree, bg="#ffffff")
frame_boutons.pack(fill=tk.X, padx=15, pady=(0, 15))

# Bouton pour insérer un exemple
bouton_exemple = tk.Button(
    frame_boutons,
    text="Charger un exemple",
    font=("Helvetica", 10),
    bg="#FF9800",
    fg="white",
    activebackground="#F57C00",
    activeforeground="white",
    relief=tk.RAISED,
    borderwidth=2,
    cursor="hand2",
    command=inserer_exemple
)
bouton_exemple.pack(side=tk.LEFT, padx=(0, 10))
bouton_exemple.bind("<Enter>", on_enter)
bouton_exemple.bind("<Leave>", lambda e: bouton_exemple.config(bg="#FF9800"))

# Bouton pour effacer
bouton_effacer = tk.Button(
    frame_boutons,
    text="Tout effacer",
    font=("Helvetica", 10),
    bg="#f44336",
    fg="white",
    activebackground="#D32F2F",
    activeforeground="white",
    relief=tk.RAISED,
    borderwidth=2,
    cursor="hand2",
    command=effacer_champs
)
bouton_effacer.pack(side=tk.LEFT)
bouton_effacer.bind("<Enter>", on_enter)
bouton_effacer.bind("<Leave>", lambda e: bouton_effacer.config(bg="#f44336"))

# Frame pour les résultats
frame_resultats = tk.LabelFrame(
    frame_principal, 
    text=" Résultats ", 
    font=("Helvetica", 12, "bold"),
    bg="#ffffff",
    fg="#333333",
    relief=tk.GROOVE,
    borderwidth=2
)
frame_resultats.pack(fill=tk.BOTH, expand=True, pady=(0, 15))

# Compteur de palindromes
label_compteur = tk.Label(
    frame_resultats,
    text="Palindromes: 0",
    font=("Helvetica", 12, "bold"),
    bg="#4CAF50",
    fg="white",
    relief=tk.RAISED,
    borderwidth=1,
    padx=15,
    pady=5
)
label_compteur.pack(anchor="ne", padx=15, pady=10)

# Zone de texte pour afficher les résultats
text_resultat = tk.Text(
    frame_resultats,
    font=("Helvetica", 11),
    bg="#FAFAFA",
    fg="#333333",
    relief=tk.SOLID,
    borderwidth=1,
    wrap=tk.WORD,
    height=10
)
text_resultat.pack(fill=tk.BOTH, expand=True, padx=15, pady=(0, 15))

# Ajouter une barre de défilement pour la zone de résultats
scrollbar = tk.Scrollbar(text_resultat)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
text_resultat.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=text_resultat.yview)

# Frame pour le bouton de recherche
frame_recherche = tk.Frame(frame_principal, bg="#f5f5f5")
frame_recherche.pack(fill=tk.X, pady=(0, 10))

# Bouton de recherche principal
bouton_rechercher = tk.Button(
    frame_recherche,
    text="TROUVER LES PALINDROMES",
    font=("Helvetica", 14, "bold"),
    bg="#2196F3",
    fg="white",
    activebackground="#1976D2",
    activeforeground="white",
    relief=tk.RAISED,
    borderwidth=3,
    cursor="hand2",
    padx=30,
    pady=12,
    command=trouver_palindromes
)
bouton_rechercher.pack()
bouton_rechercher.bind("<Enter>", on_enter)
bouton_rechercher.bind("<Leave>", on_leave)

# Exemples de palindromes
frame_exemples = tk.Frame(frame_principal, bg="#E8F5E9", relief=tk.SOLID, borderwidth=1)
frame_exemples.pack(fill=tk.X, pady=(10, 0))

label_exemples = tk.Label(
    frame_exemples,
    text="Exemples de palindromes: 121, 1331, 12321, 45654, 1001, 99, 555, 1234321, 7",
    font=("Helvetica", 10, "italic"),
    bg="#E8F5E9",
    fg="#2E7D32",
    pady=8
)
label_exemples.pack()

# Pied de page
frame_pied = tk.Frame(root, bg="#37474F", height=40)
frame_pied.pack(fill=tk.X, side=tk.BOTTOM)
frame_pied.pack_propagate(False)

label_pied = tk.Label(
    frame_pied,
    text="Réversibilité de nombres - Palindrome numérique | Interface créée avec Tkinter",
    font=("Helvetica", 9),
    bg="#37474F",
    fg="#CFD8DC"
)
label_pied.pack(expand=True)

# Insérer un exemple par défaut
inserer_exemple()

# Lancer l'application
root.mainloop()