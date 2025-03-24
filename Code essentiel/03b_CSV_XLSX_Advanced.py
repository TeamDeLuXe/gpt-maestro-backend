import pandas as pd

# Fusion de deux fichiers avec traitement
f1 = pd.read_csv('fichier1.csv')
f2 = pd.read_excel('fichier2.xlsx')

merged = pd.merge(f1, f2, on='id', how='outer')
merged.drop_duplicates(inplace=True)
merged.to_excel('resultat_final.xlsx', index=False)