def factorial(n):
    if n >= 0:
        # Termination condition
        if n == 1 or n == 0:
            return 1
        # Recursive condition
        else:
            return n * factorial(n - 1)
    else:
        return "Factorial can't be calculated for the negative numbers"


print(factorial(5))
