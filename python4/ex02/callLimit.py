def callLimit(limit: int):
    """A wrapper that limit the number of time a function can be called"""
    count = 0

    def callLimiter(function):
        """call limit function"""
        def limit_function(*args: any, **kwds: any):
            """Throw exception when limit is achieved"""
            try:
                nonlocal count
                if count >= limit:
                    raise Exception(f"{function}")
                count += 1
                return function(*args, **kwds)
            except Exception as e:
                name = function.__name__
                print(f"Error: <function {name} at{e}> call too many times")
        return limit_function
    return callLimiter
