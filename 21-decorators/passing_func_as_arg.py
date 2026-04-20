import sys

def avg(*args):
    if not args:
        return 0

    counter = 0
    sum = 0
    for arg in args:
        sum += float(arg)
        counter += 1
    return sum / counter


# def parse_args(argv):
#     if argv[1] == "max":
#         return max(*[float(number) for number in argv[2:]])
#
#     if argv[1] == "min":
#         return min(*[float(number) for number in argv[2:]])
#
#     if argv[1] == "avg":
#         return avg(*[float(number) for number in argv[2:]])

def aggr_func(func_name):
    if func_name == "max":
        return max
    if func_name == "min":
        return min
    if func_name == "avg":
        return avg

def parse_args(argv):
    aggrf = aggr_func(argv[1])
    return aggrf(*[float(number) for number in argv[2:]])

print("argv preview:")
print(sys.argv)

print()
result = parse_args(sys.argv)
print(result)