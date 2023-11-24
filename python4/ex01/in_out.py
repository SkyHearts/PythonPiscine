def square(x: int | float) -> int | float:
    """Squares a number"""
    return float(x ** 2)


def pow(x: int | float) -> int | float:
    """Power a number"""
    return float(x ** x)


def outer(x: int | float, function) -> object:
    """Return an object with a updated value"""
    count = 0

    def inner() -> float:
        nonlocal count, x
        count += 1
        ret = function(x)
        x = ret
        return ret
    return inner
