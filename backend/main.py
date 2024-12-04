import logging
from data_acquisition.fetch_papers import fetch_recent_papers
from data_processing.process_papers import extract_text_from_pdf, preprocess_text
from nlp_analysis.analyze_papers import extract_keywords
from model_adaptation.build_model import build_dynamic_model
import torch
# Setup logging
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    handlers=[logging.FileHandler('neurAI_explorer.log'),
                              logging.StreamHandler()])

logger = logging.getLogger(__name__)



def main():
    logger.info("Starting NeurAI Explorer...")
    
    try:
        papers = fetch_recent_papers()
        for paper in papers:
            try:
                logger.info(f"Processing paper: {paper['title']}")
                pdf_text = extract_text_from_pdf(paper['pdf_url'])
                processed_text = preprocess_text(pdf_text)
                keywords = extract_keywords(processed_text)
                model = build_dynamic_model(keywords)
                
                logger.info(f"Model successfully built for {paper['title']}")
            except Exception as e:
                logger.error(f"Failed to process paper {paper['title']}: {e}")
    except Exception as e:
        logger.critical(f"Critical error during the workflow: {e}")

if __name__ == "__main__":
    main()
