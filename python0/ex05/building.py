import sys


def ispunct(ch):
    """Return True if is punctuation"""
    punc = r'''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    if ch in punc:
        return True
    else:
        return False


def main():
    """Count and return the number of characthers and their type"""
# your tests and your error handling
    try:
        argc = len(sys.argv)
        assert argc <= 2, "more than one argument is provided"
        if argc == 1:
            print("What is the text to count?")
            arg = str(sys.stdin.readline())
        else:
            arg = sys.argv[1]
        c_num = len(arg)
        d = {"UPPER": 0, "LOWER": 0, "PUNCT": 0, "SPACE": 0, "DIGIT": 0}
        for c in arg:
            if c.isupper():
                d["UPPER"] += 1
            elif c.islower():
                d["LOWER"] += 1
            elif ispunct(c):
                d["PUNCT"] += 1
            elif c.isspace():
                d["SPACE"] += 1
            elif c.isdigit():
                d["DIGIT"] += 1
        print(f"The text contains {c_num} characters:")
        print(d["UPPER"], "upper letters")
        print(d["LOWER"], "lower letters")
        print(d["PUNCT"], "punctuation marks")
        print(d["SPACE"], "spaces")
        print(d["DIGIT"], "digits")
    except AssertionError as msg:
        print("AssertionError:", msg)


# your tests and your error handling
if __name__ == "__main__":
    main()

# $>python building.py "Python 3.0, released in 2008, was a major /
# revision that is not completely backward-compatible with earlier /
# versions. Python 2 was discontinued with version 2.7.18 in 2020."
# The text contains 171 characters:
# 2 upper letters
# 121 lower letters
# 8 punctuation marks
# 25 spaces
# 15 digits
# $>
