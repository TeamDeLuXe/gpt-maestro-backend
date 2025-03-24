from flask import Flask, jsonify, request, send_from_directory
import os

app = Flask(__name__)

# ✅ Route principale de test
@app.route('/')
def index():
    return jsonify({
        "message": "✅ GPT Maestro Backend est actif et prêt à recevoir des requêtes."
    })

# ✅ Route pour tester l’uptime du serveur
@app.route('/ping')
def ping():
    return jsonify({"ping": "pong"})

# ✅ Route pour servir le fichier OpenAPI YAML
@app.route('/openapi.yaml')
def serve_openapi():
    return send_from_directory(directory=os.path.dirname(__file__), path='gpt_maestro_combined_openapi.yaml', mimetype='text/yaml')

# ✅ Exemple de route API : récupérer les posts WordPress
@app.route('/wp/posts', methods=['GET'])
def get_wp_posts():
    site_url = request.args.get('site_url')
    per_page = request.args.get('per_page', default=5, type=int)

    # ❗ Ici, ajoute ton appel API réel à WordPress si besoin
    return jsonify({
        "posts": [
            {"title": f"Exemple article {i+1}", "link": f"{site_url}/article-{i+1}"}
            for i in range(per_page)
        ]
    })

# ✅ Exemple d’ajout de ligne à Google Sheets (mock, à adapter)
@app.route('/google/sheets/append', methods=['POST'])
def push_to_google_sheets():
    data = request.get_json()
    sheet_id = data.get("sheet_id")
    range_ = data.get("range")
    values = data.get("values")

    # ❗ Ici, ajoute ton appel à Google API si besoin
    return jsonify({
        "success": True,
        "message": f"Ligne ajoutée à {sheet_id} dans la plage {range_}",
        "values": values
    })

# ✅ Scraping PagesJaunes (mock)
@app.route('/scrape/pagesjaunes', methods=['GET'])
def scrape_pagesjaunes():
    keyword = request.args.get('keyword')
    city = request.args.get('city')

    return jsonify({
        "results": [
            {"name": f"{keyword.title()} Pro {i+1}", "location": city}
            for i in range(3)
        ]
    })

# ✅ Scraping Kompass (mock)
@app.route('/scrape/kompass', methods=['GET'])
def scrape_kompass():
    url = request.args.get('url')

    return jsonify({
        "category_url": url,
        "results": [
            {"name": f"Entreprise Kompass {i+1}", "url": f"{url}/entreprise-{i+1}"}
            for i in range(3)
        ]
    })

# ✅ Lancer l’app en mode développement local
if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
