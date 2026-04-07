
# x = 0
# def some_function(x):
#     x += 1
#     return x
#
# x = some_function(x)
# print(x)
#
# x = some_function(x)
# print(x)
#
# x = some_function(x)
# print(x)

def simple_generator():
    yield 1
    yield 2
    yield 3

gen = simple_generator()
print(gen)

print(next(gen))
print(next(gen))
print(next(gen))

gen2 = simple_generator()

for value in gen2:
    print(value)
