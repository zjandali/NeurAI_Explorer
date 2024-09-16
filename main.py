# main.py
from data_acquisition.fetch_papers import fetch_recent_papers
from data_processing.process_papers import extract_text_from_pdf, preprocess_text
from nlp_analysis.analyze_papers import extract_keywords
from model_adaptation.build_model import build_dynamic_model

def main():
    # Step 1: Fetch recent papers
    papers = fetch_recent_papers()
    
    for paper in papers:
        try:
            # Step 2: Extract and preprocess text
            pdf_text = extract_text_from_pdf(paper['pdf_url'])
            processed_text = preprocess_text(pdf_text)
            
            # Step 3: Extract keywords using NLP
            keywords = extract_keywords(processed_text)
            print(f"Keywords for '{paper['title']}': {keywords}")
            
            # Step 4: Build or adapt model based on keywords
            model = build_dynamic_model(keywords)
            print(f"Built model for '{paper['title']}':\n{model}\n")
            
            # (Optional) Save or deploy the model
            # save_model(model, paper['title'])
            
        except Exception as e:
            print(f"Failed to process paper '{paper['title']}': {e}")

if __name__ == "__main__":
    main()
