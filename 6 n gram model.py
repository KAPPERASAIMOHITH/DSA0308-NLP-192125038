import random

def create_bigram_model(text):
    words = text.split()
    bigrams = {}
    for i in range(len(words)-1):
        current_word = words[i]
        next_word = words[i+1]
        if current_word not in bigrams:
            bigrams[current_word] = []
        bigrams[current_word].append(next_word)
    return bigrams

def generate_text(bigrams, length=50):
    current_word = random.choice(list(bigrams.keys()))
    text = current_word
    for _ in range(length-1):
        if current_word in bigrams:
            next_word = random.choice(bigrams[current_word])
            text += " " + next_word
            current_word = next_word
        else:
            break
    return text

# Example usage
text = "I like to eat ice cream. Ice cream is delicious. I eat ice cream every day."
bigram_model = create_bigram_model(text)
generated_text = generate_text(bigram_model)
print(generated_text)
