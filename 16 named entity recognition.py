import spacy

# Download the English language model
# You need to run this command only once
# python -m spacy download en_core_web_sm

# Load the English language model
nlp = spacy.load("en_core_web_sm")

def perform_ner(text):
    # Process the text with SpaCy
    doc = nlp(text)
    
    # Iterate over entities found in the text
    for ent in doc.ents:
        print(f"Entity: {ent.text}, Type: {ent.label_}")

# Example text
example_text = "Apple Inc. is an American multinational technology company headquartered in Cupertino, California."

# Perform NER on the example text
perform_ner(example_text)
