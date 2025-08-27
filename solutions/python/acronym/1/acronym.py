def abbreviate(words):
    return "".join(give_capital(word) for word in words.replace("-", " ").split())

def give_capital(word):
    for char in word:
        if char.isalpha():
            return char.upper()

    return ""
