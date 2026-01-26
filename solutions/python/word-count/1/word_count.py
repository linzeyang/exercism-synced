from collections import Counter

def count_words(sentence):
    return Counter(part.strip("\"\'.,:!&@$%^?'") for part in sentence.lower().replace(",", " ").replace("_", " ").split())
