import time

def cache_decorator(function):
    cache = {}

    def wrapper(*args):
        if args in cache:
            print(f"Returning cached result for arguments {args}")
            return cache[args]
        else:
            result = function(*args)
            cache[args] = result
            print(f"Computing result for argument {args}")
            return result

    return wrapper

@cache_decorator
def factorial(n):
    if n == 0 or n == 1:
        return 1
    # time.sleep(1)
    return n * factorial(n - 1)


print(factorial(7))
print(factorial(7))
print(factorial(6))
print(factorial(8))