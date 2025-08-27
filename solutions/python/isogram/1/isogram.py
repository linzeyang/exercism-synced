def is_isogram(string):
    temp = set()

    for char in string:
        if not char.isalpha():
            continue
        if char.lower() not in temp:
            temp.add(char.lower())
        else:
            return False

    return True
