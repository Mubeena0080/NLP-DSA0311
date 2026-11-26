
import nltk

# Download required NLTK resources
nltk.download('punkt_tab')
nltk.download('averaged_perceptron_tagger_eng')

# Input text
text = "The cat is sleeping"

# Tokenization
tokens = nltk.word_tokenize(text)

# POS tagging
tags = nltk.pos_tag(tokens)

print("POS Tags:")
for word, tag in tags:
    print(word, ":", tag)
