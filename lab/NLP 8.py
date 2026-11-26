
from collections import Counter

training_data = [
    ("I", "PRON"), ("eat", "VERB"), ("apples", "NOUN"),
    ("You", "PRON"), ("eat", "VERB"), ("mangoes", "NOUN"),
    ("Dogs", "NOUN"), ("run", "VERB")
]

tag_counts = Counter()

for word, tag in training_data:
    tag_counts[word.lower(), tag] += 1

def tag_word(word):
    candidates = {
        tag: count
        for (known_word, tag), count in tag_counts.items()
        if known_word == word.lower()
    }

    if candidates:
        return max(candidates, key=candidates.get)
    return "UNKNOWN"

sentence = input("Enter a sentence: ")

for word in sentence.split():
    print(word, ":", tag_word(word))
