# app.py

from flask import Flask, render_template, request
import requests
import json


app = Flask(__name__)

# Homepage route
@app.route('/')
def index():
    return render_template('index.html')

# Form submission route
@app.route('/search', methods=['POST'])
def search():
    topic = request.form['topic']
    place = request.form['place']

    # Make a request to the News API
    url = 'https://newsapi.org/v2/everything'
    params = {
        'q': topic,
        'apiKey': ''  # Replace with your actual News API key
    }
    response = requests.get(url, params=params)
    data = response.json()

    # Extract place information from news data
    results = []
    for article in data['articles']:
        result = {
            'title': article.get('title', ''),
            'description': article.get('description', ''),
            'url': article.get('url', '')
        }
        results.append(result)

    total_results = len(results)
    per_page = 20
    total_pages = total_results // per_page + (total_results % per_page > 0)
    page = int(request.args.get('page', 1))

    start = (page - 1) * per_page
    end = start + per_page
    paginated_results = results[start:end]

    return render_template('result.html', results=paginated_results, page=page, total_pages=total_pages)

if __name__ == '__main__':
    app.run(debug=True)
