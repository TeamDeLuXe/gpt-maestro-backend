# 📘 README ARCHITECTURE EXEMPLES



---

## 📄 EXEMPLES_ENTREE_SORTIE.md

# 📊 Exemples types d'entrée/sortie

## Exemple 1 – CSV à nettoyer
**Entrée :** fichier `donnees.csv` avec lignes dupliquées, valeurs manquantes  
**Sortie attendue :** fichier `donnees_clean.xlsx` sans doublons, NA gérés

## Exemple 2 – Plugin WordPress
**Entrée :** besoin de restreindre contenu par rôle utilisateur  
**Sortie :** shortcode `[role_only]` avec contrôle `current_user_can()`

## Exemple 3 – Interface utilisateur
**Entrée :** app Python avec formulaire  
**Sortie :** interface Tkinter avec boutons, validation, logs intégrés


---

## 📄 MODELE_STRUCTUREL_PROJET.md

# 🧱 Modèle de structure projet (MVC / modulaire)

## Arborescence :
/projet  
├── src/                ← Code principal  
│   ├── core/           ← Logique métier  
│   └── ui/             ← Interface (Tkinter, Streamlit)  
├── data/               ← Entrées CSV/XLSX  
├── tests/              ← Fichiers unittest / pytest  
├── docs/               ← Markdown auto-générés  
└── archives/           ← Sauvegardes

## Règles :
- Chaque module = 1 fonction principale
- Tests doivent couvrir 80% min
- Logs séparés pour erreurs et succès


---

## 📄 ARCHITECTURES_ALTERNATIVES.md

# 🔄 Exemples d’alternatives techniques

## Contexte : import/export CSV/XLSX
1. pandas
2. openpyxl
3. csv + xlrd/xlwt
4. Google Sheets API

## Contexte : UI graphique Python
1. Tkinter
2. Streamlit
3. PyQt
4. Kivy

## Contexte : API backend
1. Flask
2. Django REST
3. FastAPI
4. NodeJS + Express
