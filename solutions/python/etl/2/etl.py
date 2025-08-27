def transform(legacy_data):
    return {
        char.lower(): point
        for point, chars in legacy_data.items()
        for char in chars
    }
