def append(list1, list2):
    for item in list2:
        list1.append(item)

    return list1


def concat(lists):
    if not lists:
        return []

    out = lists[0]

    for l in lists[1:]:
        out += l

    return out


def filter(function, list):
    return [item for item in list if function(item)]


def length(list):
    count = 0

    for item in list:
        count += 1

    return count


def map(function, list):
    return [function(item) for item in list]


def foldl(function, list, initial):
    for item in list:
        initial = function(initial, item)

    return initial


def foldr(function, list, initial):
    for item in list[::-1]:
        initial = function(item, initial)

    return initial


def reverse(list):
    out = []

    for i in range(len(list)):
        out.append(list[-i - 1])

    return out
