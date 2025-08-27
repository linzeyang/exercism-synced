def rebase(input_base: int, digits: list[int], output_base: int) -> list[int]:
    if input_base < 2:
        raise ValueError("input base must be >= 2")
    if any((i < 0 or i >= input_base) for i in digits):
        raise ValueError("all digits must satisfy 0 <= d < input base")
    if output_base < 2:
        raise ValueError("output base must be >= 2")

    base_10 = sum(digits[-i - 1] * input_base ** i for i in range(len(digits)))

    if base_10 == 0:
        return [0]

    if output_base == 10:
        return [int(d) for d in str(base_10)]

    out = []

    while base_10 > 0:
        out.append(base_10 % output_base)
        base_10 //= output_base

    return out[::-1]
