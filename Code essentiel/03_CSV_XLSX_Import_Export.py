import pandas as pd

# Import CSV
csv_data = pd.read_csv('fichier.csv')

# Export Excel
csv_data.to_excel('fichier_export.xlsx', index=False)