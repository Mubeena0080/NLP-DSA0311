
import random

text = "I love natural language processing. I love Python programming."
words = text.lower().replace(".", "").split()

bigrams = {}

for i in range(len(words) - 1):
    first = words[i]
    second = words[i + 1]
    bigrams.setdefault(first, []).append(second)

word = "i"
result = [word]

for _ in range(8):
    if word not in bigrams:
        break
    word = random.choice(bigrams[word])
    result.append(word)

print("Generated Text:", " ".join(result))
