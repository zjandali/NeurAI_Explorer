from transformers import pipeline

# Initialize a transformer pipeline for keyword extraction
keyword_extractor = pipeline("ner", model="dbmdz/bert-large-cased-finetuned-conll03-english")

def extract_keywords(text):
    ner_results = keyword_extractor(text)
    keywords = set()
    for entity in ner_results:
        if entity['entity'] in ['B-MISC', 'I-MISC', 'B-ORG', 'I-ORG', 'B-PER', 'I-PER']:
            keywords.add(entity['word'])
    return list(keywords)
