
def initial_tag(word):
    if word.lower() in ["is", "am", "are", "was", "run", "eat"]:
        return "VERB"
    return "NOUN"

def transform_tag(word, tag, previous_word):
    # Transformation rule: "to" followed by a word -> verb
    if previous_word.lower() == "to":
        return "VERB"
    return tag

sentence = input("Enter a sentence: ")
words = sentence.split()

previous_word = ""

for word in words:
    tag = initial_tag(word)
    tag = transform_tag(word, tag, previous_word)
    print(word, ":", tag)
    previous_word = word
