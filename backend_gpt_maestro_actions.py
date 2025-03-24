from flask import Flask, request, jsonify, abort
from flask_cors import CORS
import random
import os
import datetime

app = Flask(__name__)
CORS(app)

API_TOKEN = os.getenv("GPT_API_TOKEN", "mon_token_local")

@app.before_request
def check_auth():
    if request.headers.get("Authorization") != f"Bearer {API_TOKEN}":
        abort(401)

@app.route('/wp/posts', methods=['GET'])
def get_wp_posts():
    site_url = request.args.get('site_url')
    per_page = int(request.args.get('per_page', 5))
    return jsonify({
        "posts": [
            {"title": f"Article {i+1}", "link": f"{site_url}/article-{i+1}"}
            for i in range(per_page)
        ]
    })

@app.route('/google/sheets/append', methods=['POST'])
def push_to_google_sheets():
    data = request.json
    return jsonify({
        "success": True,
        "message": f"Ligne insérée dans {data.get('sheet_id')} à {data.get('range')}"
    })

@app.route('/scrape/pagesjaunes', methods=['GET'])
def scrape_pagesjaunes():
    city = request.args.get('city')
    keyword = request.args.get('keyword')
    return jsonify({
        "results": [f"{keyword.title()} Pro {i+1} à {city}" for i in range(5)]
    })

@app.route('/scrape/kompass', methods=['GET'])
def scrape_kompass():
    url = request.args.get('url')
    return jsonify({
        "results": [f"Entreprise extraite de {url} – ligne {i+1}" for i in range(10)]
    })

@app.route('/csv/summarize', methods=['POST'])
def summarize_csv_row():
    content = request.json.get("content", "")
    bullets = content.split(".")[:3]
    return jsonify({"summary": [s.strip() for s in bullets if s.strip()]})

@app.route('/seo/meta', methods=['GET'])
def get_meta_tags():
    url = request.args.get('url')
    return jsonify({
        "title": "Titre simulé pour SEO",
        "description": "Description optimisée générée automatiquement.",
        "keywords": "sécurité, surveillance, entreprise"
    })

@app.route('/csv/autotag', methods=['POST'])
def auto_tag_csv():
    row = request.json.get("row", "")
    tags = []
    if "sécurité" in row.lower():
        tags.append("Sécurité")
    if "incendie" in row.lower():
        tags.append("SSIAP")
    return jsonify({"tags": tags})

@app.route('/geo/coordinates', methods=['GET'])
def build_coordinates():
    address = request.args.get("address")
    return jsonify({
        "lat": 45.75 + random.uniform(-0.01, 0.01),
        "lng": 4.85 + random.uniform(-0.01, 0.01),
        "source": "simulation"
    })

@app.route('/generate/markdown-profile', methods=['POST'])
def generate_markdown_profile():
    data = request.json
    name = data.get("name", "Entreprise")
    description = data.get("description", "Description non fournie.")
    markdown = f"# {name}\n\n{description}\n\n- 📍 Généré automatiquement"
    return jsonify({"markdown": markdown})

@app.route('/text/clean', methods=['POST'])
def clean_text():
    html = request.json.get("html", "")
    text = html.replace("<", "").replace(">", "").replace("/", "").replace("script", "")
    return jsonify({"cleaned": text})

@app.route('/batch/urls-meta', methods=['POST'])
def batch_urls_meta():
    urls = request.json.get("urls", [])
    return jsonify({
        "results": [
            {"url": url, "title": f"Title for {url}", "description": "Auto-desc", "keywords": "test, seo"}
            for url in urls
        ]
    })

@app.route('/log/trace', methods=['POST'])
def log_trace():
    trace = {
        "timestamp": datetime.datetime.now().isoformat(),
        "endpoint": request.path,
        "method": request.method,
        "params": request.args if request.args else request.json
    }
    return jsonify({"trace": trace, "status": "logged"})

if __name__ == '__main__':
    app.run(debug=True, port=5001)
