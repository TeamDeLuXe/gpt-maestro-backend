from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/wp/posts', methods=['GET'])
def get_wp_posts():
    site_url = request.args.get('site_url')
    per_page = request.args.get('per_page', 5)
    return jsonify({
        "posts": [
            {"title": "Article 1", "link": f"{site_url}/article-1"},
            {"title": "Article 2", "link": f"{site_url}/article-2"}
        ]
    })

@app.route('/google/sheets/append', methods=['POST'])
def push_to_google_sheets():
    data = request.get_json()
    return jsonify({
        "success": True,
        "message": f"Ligne ajoutée à la feuille {data.get('sheet_id')} à la plage {data.get('range')}"
    })

@app.route('/scrape/pagesjaunes', methods=['GET'])
def scrape_pagesjaunes():
    keyword = request.args.get('keyword')
    city = request.args.get('city')
    return jsonify({
        "results": [
            {"name": f"{keyword} Pro 1", "city": city},
            {"name": f"{keyword} Pro 2", "city": city}
        ]
    })

@app.route('/scrape/kompass', methods=['GET'])
def scrape_kompass():
    url = request.args.get('url')
    return jsonify({
        "results": [
            {"company": "Kompass Company A", "url": url},
            {"company": "Kompass Company B", "url": url}
        ]
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)