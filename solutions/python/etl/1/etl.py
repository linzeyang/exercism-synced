def transform(legacy_data):
    out = {}

    for point, chars in legacy_data.items():
        for char in chars:
            out[char.lower()] = point

    return out
