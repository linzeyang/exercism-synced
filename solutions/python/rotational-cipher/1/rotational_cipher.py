def rotate(text, key):
    if key in {0, 26}:
        return text

    from string import ascii_lowercase, ascii_uppercase

    lower = ascii_lowercase[key:] + ascii_lowercase[:key]
    upper = ascii_uppercase[key:] + ascii_uppercase[:key]

    mapping = dict(zip(ascii_lowercase + ascii_uppercase, lower + upper))

    return "".join(mapping.get(char, char) for char in text)
