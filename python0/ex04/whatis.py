import sys

argc = len(sys.argv)
if argc != 1:
    try:
        assert argc == 2, "more than one argument is provided"
        arg = sys.argv[1]
        flag = False
        if (arg.lstrip("-").isdigit()):
            flag = True
        assert flag is True, "argument is not an integer"
        num = int(arg)
        if num % 2 == 0:
            print("I'm Even.")
        else:
            print("I'm Odd.")
    except AssertionError as msg:
        print("AssertionError:", msg)
