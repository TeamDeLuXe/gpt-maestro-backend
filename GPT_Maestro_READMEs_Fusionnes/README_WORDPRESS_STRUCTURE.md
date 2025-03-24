# 📘 README WORDPRESS STRUCTURE



---

## 📄 06_WordPress_Theme_Structure.md

# Hiérarchie des templates WordPress

- `index.php`: fallback général
- `single.php`: articles
- `page.php`: pages
- `archive.php`: archives
- `functions.php`: logique PHP globale


---

## 📄 06b_Theme_WordPress_Structure_Avancee.md

# Structure Avancée Thème WordPress

- Template parts (`template-parts/`)
- Fichiers conditionnels (`category-news.php`, `single-product.php`)
- `functions.php` avec hooks personnalisés
- Chargement conditionnel des scripts/styles
- Utilisation de `get_template_part()` et `WP_Query` avancé


---

## 📄 13_Theme_Enfant_WordPress.md

# Créer un thème enfant WordPress

1. Créer un dossier `mon-theme-enfant`
2. Ajouter `style.css` avec Template: parent-theme
3. Ajouter `functions.php` pour charger le style parent
4. Activer depuis l’admin WordPress
