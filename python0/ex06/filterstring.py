import sys
from ft_filter import ft_filter


def containpunct(string):
    """return false if contain punctuation"""

    punc = r'''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    for ch in string:
        if ch in punc:
            return True
    return False


def filterstring(S, N):
    """Uses ft_filter to filter out string > certain length"""
    split = S.split(" ")
    new_lst = list(ft_filter(lambda a: True if len(a) > N else False, split))
    print(new_lst)


def main():
    """Test string larger than"""
    # original = (filter.__doc__)
    # copy = (ft_filter.__doc__)
    # print(copy)
    # print(original == copy)
    try:
        argc = len(sys.argv)
        assert argc == 3, "the arguments are bad"
        string = sys.argv[1]
        size = sys.argv[2]
        flag = False
        if (size.lstrip("-").isdigit() and containpunct(string) is False):
            flag = True
        assert flag is True, "the arguments are bad"
        size = int(sys.argv[2])
        filterstring(string, size)
    except AssertionError as msg:
        print("AssertionError:", msg)


if __name__ == "__main__":
    main()
    # print(filter.__doc__)
