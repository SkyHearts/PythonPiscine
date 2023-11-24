def ft_filter(func, iter):
    """filter(function or None, iterable) --> filter object

Return an iterator yielding those items of iterable for which function(item)
is true. If function is None, return the items that are true."""
    # for a in iter:
    if func is None:
        return (a for a in iter)
    else:
        return (a for a in iter if func(a))


# def check_even(number):
#     if number % 2 == 0:
#         return True
#     return False


# def main():
#     int_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#     even = ft_filter(check_even, int_list)
#     even = filter(check_even, int_list)
#     even_list = list(even)
#     print(even_list)


# if __name__ == "__main__":
#     """Testing"""
#     main()
