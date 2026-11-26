
import re

patterns = [
    (r".*ing$", "VERB"),
    (r".*ed$", "VERB"),
    (r".*ly$", "ADV"),
    (r".*ous$", "ADJ"),
    (r".*s$", "NOUN"),
    (r".*", "NOUN")
]

def tag_word(word):
    for pattern, tag in patterns:
        if re.fullmatch(pattern, word.lower()):
            return tag

sentence = input("Enter a sentence: ")

for word in sentence.split():
    print(word, ":", tag_word(word))
