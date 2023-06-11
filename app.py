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
@app.route('/search', methods=['GET', 'POST'])
def search():
    if request.method == 'POST':
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

        return render_template('result.html', results=results)

    # Handle GET request
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
