'''
import nltk
from nltk.tokenize import word_tokenize

texts = [
    "the sun is shining brightly",
    "i love reading interesting books"
]

nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')

for text in texts:
    tagged_words = nltk.pos_tag(word_tokenize(text))
    print("Original Text:", text)
    print("POS Tagging:", tagged_words)
    print()
'''
'''
import spacy

nlp = spacy.load("en_core_web_sm")

sentences = [
    "Apple Inc is headquartered in Cupertino, California and its CEO Tim Cook often delivers keynote speeches.",
    "The Eiffel Tower in Paris, France, is a popular tourist attraction."
]

for sentence in sentences:
    entities = nlp(sentence).ents
    print("Sentence:", sentence)
    for entity in entities:
        print("  Entity:", entity.text)
        print("  Label:", entity.label_)
    print()
'''
'''
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

sentences = [
    "climate change is a pressing global issue that requires immediate action",
    "renewable energy sources, such as solar and wind power, are essential for reducing carbon emissions"
]

query = "climate change requires immediate action"

tfidf_matrix = TfidfVectorizer().fit_transform(sentences + [query])
ranked_sentences = sorted(zip(cosine_similarity(tfidf_matrix[-1], tfidf_matrix[:-1])[0], sentences), reverse=True)

for i, (score, sentence) in enumerate(ranked_sentences, start=1):
    print(f"Rank {i}: Score = {score:.4f}, Sentence = '{sentence}'")
'''
'''
import re


text = "the quick brown fox jumps over the lazy dog the cat is also agile"
pattern = r'\b\w{3,}\b'
matches = re.findall(pattern, text)
print("Text:", text)
print("Regular Expression Pattern:", pattern)
print("Matches found:")
for match in matches:
    print(match)

'''
