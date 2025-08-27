def append(list1, list2):
    for item in list2:
        list1.append(item)

    return list1


def concat(lists):
    out = []

    for l in lists:
        out.extend(l)

    return out


def filter(function, list):
    return [item for item in list if function(item)]


def length(list):
    return sum(1 for _ in list)


def map(function, list):
    return [function(item) for item in list]


def foldl(function, list, initial):
    for item in list:
        initial = function(initial, item)

    return initial


def foldr(function, list, initial):
    for item in list[::-1]:
        initial = function(initial, item)

    return initial


def reverse(list):
    return list[::-1]
