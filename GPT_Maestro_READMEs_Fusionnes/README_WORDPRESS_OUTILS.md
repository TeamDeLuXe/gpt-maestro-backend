# 📘 README WORDPRESS OUTILS



---

## 📄 07_WP_CLI_Cheat_Sheet.md

# WP-CLI Cheat Sheet

- `wp plugin install akismet --activate`
- `wp theme list`
- `wp user create nom email@example.com --role=editor`
- `wp export`
- `wp db export`


---

## 📄 07b_WP_CLI_Cheat_Sheet_Avance.md

# WP-CLI Avancé

- `wp post meta update` pour automatisation des champs
- `wp eval-file` pour exécuter un script PHP
- `wp db search 'texte'` pour recherche SQL
- `wp cron event list`
- `wp plugin update --all`


---

## 📄 12_WordPress_REST_API_Exemple.md

# Utilisation de la REST API WordPress

- Endpoint pour articles: `/wp-json/wp/v2/posts`
- Authentification avec JWT ou OAuth
- Créer un endpoint custom avec `register_rest_route()`
- Exemple de consommation depuis JS ou Python
