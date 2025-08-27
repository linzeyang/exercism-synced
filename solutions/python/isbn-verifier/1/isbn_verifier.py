def is_valid(isbn):
    nums = []

    for char in isbn:
        if char.isdigit():
            nums.append(int(char))
        elif char == "X":
            nums.append(10)
        elif char.isalpha():
            return False
        elif char != "-":
            return False

    if len(nums) != 10:
        return False

    if 10 in nums and nums.index(10) != 9:
        return False

    return sum(nums[i] * (10 - i) for i in range(10)) % 11 == 0
            
