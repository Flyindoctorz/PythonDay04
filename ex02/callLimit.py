def callLimit(limit: int):
    count = 0

    def callLimiter(function):

        def limit_function(*args: any, **kwds: any):
            nonlocal count
            if count < limit:
                count += 1
                function()
            else:
                print(f"Error: <function {function} call too many times")
                return
        return (limit_function)
    return (callLimiter)
