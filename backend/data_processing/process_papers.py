import requests
from io import BytesIO
import PyPDF2
import spacy

# Load spaCy model
nlp = spacy.load('en_core_web_sm')

def extract_text_from_pdf(pdf_url):
    response = requests.get(pdf_url)
    with BytesIO(response.content) as open_pdf_file:
        reader = PyPDF2.PdfReader(open_pdf_file)
        text = ''
        for page in reader.pages:
            text += page.extract_text() or ''
    return text

def preprocess_text(text):
    doc = nlp(text)
    tokens = [token.lemma_.lower() for token in doc if token.is_alpha and not token.is_stop]
    return ' '.join(tokens)
