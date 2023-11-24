from callLimit import callLimit


# @callLimit(3)
# def f():
#     print("f()")


# @callLimit(1)
# def g():
#     print("g()")


# for i in range(3):
#     f()
#     g()


# $> python tester.py
# f()
# g()
# f()
# Error: <function g at 0x7fabdc243ee0> call too many times
# f()
# Error: <function g at 0x7fabdc243ee0> call too many times
# $>

@callLimit(0)
def h():
    print("h()")


@callLimit(2)
def j():
    print("j()")


@callLimit(1)
def k():
    print("k()")


for i in range(2):
    h()
    j()
    k()
