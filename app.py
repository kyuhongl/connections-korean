from flask import Flask, jsonify
from scraper import scrape_page
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/connections', methods=['GET'])
def get_connections():
    categories, individual_words = scrape_page() 
    if categories is None or individual_words is None:
        return jsonify({"error": "Could not scrape the page"}), 500
    return jsonify({
        "categories": categories,
        "individual_words": individual_words
    })


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

