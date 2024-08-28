from flask import Flask, request, jsonify
import requests
import sqlite3

app = Flask(__name__)

# کلید API و Host برای RapidAPI
RAPIDAPI_KEY = '1c2d52b392msh514965568dc4419p15461bjsn0ecdd0667e4e'
RAPIDAPI_HOST = 'url-shortener-service.p.rapidapi.com'

def shorten_url(long_url):
    url = "https://url-shortener-service.p.rapidapi.com/shorten"

    headers = {
        "X-RapidAPI-Key": RAPIDAPI_KEY,
        "X-RapidAPI-Host": RAPIDAPI_HOST,
        "Content-Type": "application/json"
    }
    data = {
        "url": long_url
    }

    response = requests.post(url, json=data, headers=headers)
    if response.status_code == 200:
        return response.json().get("result_url")
    else:
        return None

@app.route('/shorten', methods=['POST'])
def shorten():
    if 'url' in request.json:
        long_url = request.json['url']
        short_url = shorten_url(long_url)

        db_login = sqlite3.connect('urls')
        cr_db = db_login.cursor()
        cr_db.execute("INSERT INTO urls (long_url, short_url) VALUES (?, ?);", (long_url, short_url))
        db_login.commit()

        if short_url:
            return jsonify({"short_url": short_url}), 200
        else:
            return jsonify({"error": "Failed to shorten URL"}), 500
    else:
        return jsonify({"error": "URL not provided"}), 400
    

@app.route('/shortens')
def shortens():
    long_url = "sssssszzz"
    short_url = "fdf"

    db_login = sqlite3.connect('urls')
    cr_db = db_login.cursor()
    cr_db.execute("INSERT INTO urls (long_url, short_url) VALUES (?, ?);", (long_url, short_url))
    db_login.commit()

    if short_url:
        return jsonify({"short_url": short_url}), 200
    else:
        return jsonify({"error": "Failed to shorten URL"}), 500


if __name__ == '__main__':
    app.run(debug=True)
