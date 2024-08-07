from flask import Flask, render_template, request, jsonify
from scrapping import scrape_job  

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/scrape', methods=['POST'])
def scrape():
    url = request.form['url']
    #https://jobs.careers.microsoft.com/global/en/search?q=Engineering&p=Research%2C%20Applied%2C%20%26%20Data%20Sciences&p=Software%20Engineering&exp=Students%20and%20graduates&ws=Microsoft%20on-site%20only&el=Bachelors&l=en_us&pg=1&pgSz=20&o=Relevance&flt=true
    job_class_name = "ms-List-cell"
    title_selector = 'h2.MZGzlrn8gfgSs8TZHhv2'
    jobs = scrape_job(url, job_class_name, title_selector)
    return jsonify(jobs)

if __name__ == '__main__':
    app.run(debug=True)
