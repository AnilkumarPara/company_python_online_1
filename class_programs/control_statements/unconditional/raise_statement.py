def my_function(x):
    if x < 0:
        raise ValueError("x must be non-negative")
    return x


my_function(-1)
