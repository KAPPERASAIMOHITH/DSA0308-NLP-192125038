'''
import nltk
nltk.download('treebank')
from nltk.tag import DefaultTagger, UnigramTagger, BigramTagger
from nltk.corpus import treebank

sentences = [
    "the red car stopped at the traffic light",
    "she quickly ran to catch the bus"
]

training_data = treebank.tagged_sents()[:3000]

default_tagger = DefaultTagger('NN')
unigram_tagger = UnigramTagger(training_data, backoff=default_tagger)
bigram_tagger = BigramTagger(training_data, backoff=unigram_tagger)
tagged_sentences = [bigram_tagger.tag(nltk.word_tokenize(sentence)) for sentence in sentences]

for i, sentence in enumerate(tagged_sentences):
    print(f"Sentence {i+1}:")
    print(" ".join([f"{word}/{tag}" for word, tag in sentence]))
    print()

'''
'''
import spacy

nlp = spacy.load("en_core_web_sm")

text = "The World Health Organization (WHO) plays a vital role in global health. WHO is headquartered in Geneva, Switzerland and it is responsible for coordinating international efforts to control and prevent the spread of diseases. Its mission is to promote and protect the health of people worldwide."

entities = [ent.text for ent in nlp(text).ents]
summary = " ".join(entities)

print("Generated Summary:")
print(summary)
'''
'''
import spacy

nlp = spacy.load("en_core_web_sm")

sentences = [
    "the quick brown fox jumps over the lazy dog",
    "she is an excellent chef and loves to cook delicious meals",
    "the Eiffel Tower in Paris is a famous landmark"
]

for sentence in sentences:
    doc = nlp(sentence)
    print("Sentence:", sentence)
    for chunk in doc.noun_chunks:
        print("  Noun Phrase:", chunk.text)
        print("  Meaning:", chunk.root.text)
    print()

'''
'''
import nltk
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer


nltk.download('punkt')
nltk.download('wordnet')


sentences = [
    "the quick brown foxes jumped over the lazy dogs",
    "i am running in the park with my friends"
]


lemmatizer = WordNetLemmatizer()


for sentence in sentences:
    tokens = word_tokenize(sentence)
    lemmatized_words = [lemmatizer.lemmatize(word) for word in tokens]
    
    print("Original Sentence:", sentence)
    print("Lemmatized Sentence:", " ".join(lemmatized_words))
    print()
'''
