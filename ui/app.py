from flask import Flask, render_template

import arxiv

def fetch_recent_papers(category='cs.LG', max_results=100):
    search = arxiv.Search(
        query=f"cat:{category}",
        max_results=max_results,
        sort_by=arxiv.SortCriterion.SubmittedDate
    )
    papers = []
    for result in search.results():
        papers.append({
            'title': result.title,
            'authors': [author.name for author in result.authors],
            'abstract': result.summary,
            'pdf_url': result.pdf_url,
            'published': result.published
        })
    return papers

app = Flask(__name__)

@app.route('/')
def index():
    papers = fetch_recent_papers()
    return render_template('index.html', papers=papers)

if __name__ == '__main__':
    app.run(debug=True)
