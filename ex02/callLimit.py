def callLimit(limit: int):
    """wrap and return callLimiter"""
    count = 0

    def callLimiter(function):
        """wrap and return limit_function"""
        def limit_function(*args: any, **kwds: any):
            """return either the ft either error if limit reached"""
            nonlocal count
            if count < limit:
                count += 1
                function()
            else:
                print(f"Error: <function {function} call too many times")
                return
        return (limit_function)
    return (callLimiter)
