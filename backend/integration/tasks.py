from celery import Celery
from data_acquisition.fetch_papers import fetch_recent_papers
from data_processing.process_papers import extract_text_from_pdf, preprocess_text
from nlp_analysis.analyze_papers import extract_keywords
from model_adaptation.build_model import build_dynamic_model

app = Celery('neurAI_explorer', broker='pyamqp://guest@localhost//')

@app.task
def update_models():
    papers = fetch_recent_papers()
    for paper in papers:
        try:
            pdf_text = extract_text_from_pdf(paper['pdf_url'])
            processed_text = preprocess_text(pdf_text)
            keywords = extract_keywords(processed_text)
            model = build_dynamic_model(keywords)
            # Save or deploy the model as needed
        except Exception as e:
            print(f"Error processing paper {paper['title']}: {e}")
