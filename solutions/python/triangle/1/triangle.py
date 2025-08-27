def equilateral(sides):
    a, b, c = sides
    return (a == b) and (b == c) and a > 0


def isosceles(sides):
    a, b, c = sides

    if (a + b) < c or (a + c) < b or (b + c) < a:
        return False

    return a == b or b == c or c == a


def scalene(sides):
    a, b, c = sides

    if (a + b) < c or (a + c) < b or (b + c) < a:
        return False

    return not (a == b or b == c or c == a)
