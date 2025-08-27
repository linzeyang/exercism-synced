def is_paired(input_string):
    temp = []
    for char in input_string:
        if char in "[{(":
            temp.append(char)
            continue

        if char not in ")]}":
            continue

        try:
            p = temp.pop()
        except Exception:
            return False

        if char == "]":
            if p != "[":
                return False
        elif char == "}":
            if p != "{":
                return False
        elif char == ")":
            if p != "(":
                return False

    return temp == []
