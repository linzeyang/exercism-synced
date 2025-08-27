def flatten(iterable):
    out = []

    for item in iterable:
        if item is None:
            continue
        if not isinstance(item, (list, tuple, set)):
            out.append(item)
        else:
            out.extend(flatten(item))

    return out
