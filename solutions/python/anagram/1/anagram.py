def find_anagrams(word, candidates):
    return [w for w in candidates if is_anagram(word, w)]

def is_anagram(a, b):
    if a.lower() == b.lower():
        return False
    return sorted(a.lower()) == sorted(b.lower())