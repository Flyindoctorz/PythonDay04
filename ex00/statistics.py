def get_mean(*args):
    """get the mean"""
    res = sum(args) / len(args)
    return (res)


def get_median(*args):
    """get the median"""
    res = 0
    sorted_args = sorted(args)
    mid = len(args) // 2
    if len(args) % 2 == 1:
        res = sorted_args[mid]
    else:
        res = (sorted_args[1] + sorted_args[2]) / 2
    return (res)


def get_quartile(*args):
    """get Q1 and Q3"""
    res = 0
    sorted_args = sorted(args)
    q1 = int(len(args) * 0.25)
    q3 = int(len(args) * 0.75)
    res = [float(sorted_args[q1]), float(sorted_args[q3])]
    return (res)


def get_var(*args):
    """get the variance"""
    total = 0
    mean = get_mean(*args)
    for elem in args:
        total += (elem - mean)**2
    var = total / len(args)
    return (var)


def get_std(*args):
    """get the standard deviation"""
    var = get_var(*args)
    return (var)**0.5


def ft_statistics(*args: any, **kwargs: any) -> None:
    """Make some stats"""
    for key, value in kwargs.items():
        if args:
            if value == "mean":
                res = get_mean(*args)
                print(f"mean : {res}")
            elif value == "median":
                res = get_median(*args)
                print(f"median : {res}")
            elif value == "quartile":
                res = get_quartile(*args)
                print(f"quartile : {res}")
            elif value == "var":
                res = get_var(*args)
                print(f"var : {res}")
            elif value == "std":
                res = get_std(*args)
                print(f"std : {res}")
        else:
            print("ERROR")
