import os
from datetime import datetime
import shutil

def generer_index(dossier_path, nom_fichier='GPT_MAESTRO_INDEX_AUTOMATIQUE.md'):
    extensions = {
        '.py': '🐍 Scripts Python',
        '.php': '🔌 Plugins WordPress (PHP)',
        '.md': '📄 Fichiers Markdown (Docs)',
        '.txt': '🧱 Notes / Structures',
        '.csv': '📊 Données CSV',
        '.json': '🔧 Fichiers JSON / config'
    }

    fichiers = os.listdir(dossier_path)
    index_content = f"# 📁 Index Automatique de `{dossier_path}`\n\n"
    index_content += f"🕒 Généré le {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n"
    index_content += "Ce fichier est généré automatiquement. Il classe les fichiers par type pour t’aider à t’y retrouver.\n\n"

    for ext, titre in extensions.items():
        groupe = sorted([f for f in fichiers if f.endswith(ext)])
        if groupe:
            index_content += f"## {titre}\n"
            for f in groupe:
                index_content += f"- `{f}`\n"
            index_content += "\n"

    autres = [f for f in fichiers if os.path.isfile(os.path.join(dossier_path, f)) and not any(f.endswith(e) for e in extensions)]
    if autres:
        index_content += "## 📦 Autres fichiers\n"
        for f in sorted(autres):
            index_content += f"- `{f}`\n"

    # Sauvegarde ancienne version si présente
    chemin_index = os.path.join(dossier_path, nom_fichier)
    if os.path.exists(chemin_index):
        horodatage = datetime.now().strftime("%Y%m%d_%H%M%S")
        backup_path = os.path.join(dossier_path, f"OLD_{nom_fichier.replace('.md', f'_{horodatage}.md')}")
        shutil.copy2(chemin_index, backup_path)
        print(f"🔁 Ancien index sauvegardé : {backup_path}")

    with open(chemin_index, "w", encoding="utf-8") as f:
        f.write(index_content)

    print(f"✅ Index généré : {chemin_index}")

# Utilisation sans console
if __name__ == '__main__':
    dossier_cible = os.path.dirname(os.path.abspath(__file__))
    generer_index(dossier_cible)
