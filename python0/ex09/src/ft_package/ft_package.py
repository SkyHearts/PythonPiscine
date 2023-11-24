def count_in_list(lst: list, find: str) -> int:
    """Just show if function works"""
    count = 0
    for item in lst:
        if item == find:
            count += 1
    return count
