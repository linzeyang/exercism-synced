def triplets_with_sum(number):
    out = []

    for c in range(number // 3 + 1, number - 2):
        c_sq = c ** 2
        for a in range((number - c) // 2, 0, -1):
            b = number - a - c

            if a >= b or b >= c:
                continue

            if a ** 2 + b ** 2 == c_sq:
                out.append([a, b, c])
                break

    return out
