def ft_mean(lst: list) -> int | float:
    """Return mean"""
    # if (len(lst) == 0):
    #     print("ERROR")
    # else:
    number_of_data = len(lst)
    mean = sum(lst) / number_of_data
    return mean


def ft_median(lst: list) -> int | float:
    """Return median"""
    # if (len(lst) == 0):
    #     print("ERROR")
    # else:
    number_of_data = len(lst)
    sorted_lst = sorted(lst)
    median = 0
    mid = int(number_of_data/2)
    if (number_of_data % 2 == 0):
        median = (sorted_lst[mid - 1] + sorted_lst[mid]) / 2
    else:
        median = sorted_lst[mid]
    return median


def ft_quartile(lst: list) -> list | float:
    """Return quartile"""
    # if (len(lst) == 0):
    #     print("ERROR")
    # else:
    quartile_lst = []
    sorted_lst = sorted(lst)
    middle = len(sorted_lst)//2
    lower_quartile = float(ft_median(sorted_lst[:middle + 1]))
    quartile_lst.append(lower_quartile)
    upper_quartile = float(ft_median(sorted_lst[middle:]))
    quartile_lst.append(upper_quartile)
    return quartile_lst


def ft_SD(lst: list) -> float:
    """Return standard deviation"""
    number_of_data = len(lst)
    mean = ft_mean(lst)
    sumof = 0
    for item in lst:
        sumof += (item - mean) ** 2
    SD = (sumof / number_of_data) ** 0.5
    return SD


def ft_statistics(*args: any, **kwargs: any) -> None:
    """Prints out statistic mean,median,quartile,sd and var"""
    try:
        argc = 0
        lst = []
        for item in args:
            argc += 1
            lst.append(item)
        # sorted_lst = sorted(lst)
        # print(sorted_lst)
        for key, value in kwargs.items():
            if (len(lst) <= 0):
                print("ERROR")
            elif (value == "mean" and len(lst) > 0):
                print("mean:", ft_mean(lst))
            elif (value == "median" and len(lst) > 1):
                print("median:", ft_median(lst))
            elif (value == "quartile" and len(lst) > 2):
                print("quartile:", ft_quartile(lst))
            elif (value == "std" and len(lst) > 1):
                print("std:", ft_SD(lst))
            elif (value == "var" and len(lst) > 1):
                print("var:", ft_SD(lst) ** 2)
    except AssertionError as msg:
        print(msg)
