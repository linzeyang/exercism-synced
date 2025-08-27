def is_pangram(sentence):
    temp = set(char.lower() for char in sentence if char.isalpha())
    return len(temp) == 26
