from flask import Flask, render_template, request, jsonify
from scrapping import scrape_job  
import json

app = Flask(__name__)

def load_company_data(filename='companies.json'):
    with open(filename, 'r') as file:
        companies = json.load(file)
    return companies['companies']

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/scrape', methods=['POST'])
def scrape():
    companies = load_company_data()
    all_jobs = {}
    for company, details in companies.items():
        jobs = scrape_job(details)
        all_jobs[company] = jobs
    return jsonify(all_jobs)

if __name__ == '__main__':
    app.run(debug=True)
