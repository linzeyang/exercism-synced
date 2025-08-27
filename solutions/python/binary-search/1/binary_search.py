def find(search_list, value):
    if not search_list:
        raise ValueError("value not in array")

    mid_idx = len(search_list) // 2

    if search_list[mid_idx] == value:
        return mid_idx

    if search_list[mid_idx] < value:
        return mid_idx + 1 + find(search_list[mid_idx + 1:], value)

    return find(search_list[:mid_idx], value)
