'''
import re

patterns = [
    (r'\b(Ilic|the)\b', 'DET'),
    (r'\b(is|am|are)\b', 'VERB'),
    (r'\b(quick|bright)\b', 'ADV'),
    (r'\b(cat|dog)\b', 'NOUN'),
]

text = "the quick brown cat is sleeping"

tagged_words = [(word, tag) for word in text.split() for pattern, tag in patterns if re.match(pattern, word, re.IGNORECASE)] or [(word, 'NOUN') for word in text.split()]

for word, tag in tagged_words:
    print(f"{word}: {tag}")
'''
'''
import spacy

nlp = spacy.load("en_core_web_sm")

sentence = "The capital of France is Paris, and it's known for the Eiffel Tower."

for ent in nlp(sentence).ents:
    print(f"{ent.text}: {ent.label_}")
'''
'''
import nltk
pcfg_grammar = nltk.PCFG.fromstring("""
    S -> NP VP [1.0]
    NP -> Det N [0.511] | NP PP [0.4] | 'the' [0.089]
    VP -> V NP [0.7] | VP PP [0.3]
    PP -> P NP [1.0]
    Det -> 'the' [0.71] | 'a' [0.3]
    N -> 'fox' [0.4] | 'dog' [0.3] | 'cat' [0.2] | 'bird' [0.1]
    V -> 'jumps' [0.51] | 'runs' [0.31] | 'sits' [0.18]
    P -> 'over' [0.6] | 'on' [0.4]
""")
parser = nltk.ViterbiParser(pcfg_grammar)
sentence = "The quick brown fox jumps over the lazy dog."
tokens = nltk.word_tokenize(sentence)
parses = parser.parse(tokens)
for tree in parses:
    print(tree)
'''
'''
import nltk
from nltk.stem import PorterStemmer

stemmer = PorterStemmer()

sentences = [
    "Coding with Python is very enjoyable.",
    "I had a delicious meal at the restaurant."
]

for sentence in sentences:
    print("Original Sentence:", sentence)
    print("Stemmed Sentence:", " ".join(stemmer.stem(word) for word in nltk.word_tokenize(sentence)))
    print()
'''
