def commands(binary_str):
    out = []

    for idx, digit in enumerate(binary_str[::-1]):
        if idx == 0 and digit == "1":
            out.append("wink")
        if idx == 1 and digit == "1":
            out.append("double blink")
        if idx == 2 and digit == "1":
            out.append("close your eyes")
        if idx == 3 and digit == "1":
            out.append("jump")
        if idx == 4 and digit == "1":
            out.reverse()
    return out
