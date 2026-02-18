
msg = """Hello Jakub! 
Nice to meet you! 
End of program"""

print(msg)

print()

msg = "Good bye Jakub!"
print(msg)

print()

a = 1
b = 2
print(a)
print(b)
print(a + b)
print()

print(1)
print(2)
print(1 + 2)

print()
msg1 = "Hello Jakub!"
msg2 = "Nice to meet you!"
print(msg1 + " " + msg2)
print()

msg_start = "Hello "
msg_end = "! Nice to meet you!"
name = "Jakub"

print(msg_start + name + msg_end)

print()

print(1+2)
print(2*3)

print()

name1 = "Jakub"
name2 = "Mark"
print(name1 * 10)
print(name2 * 10)

print()

print("-" * 200)
print("#" * 20 + " Strings as a templates " + "#" * 20)
print()

name = "Melisa"
count = 100

# Option 1
msg = "Hello " + name + "! This is your day number " + str(count) + " with us! Thank you for being here!"
print(msg)

print()
print("-" * 20 + "NEXT DAY" + "-" * 20)
count = count + 1
print()

msg = "Hello " + name + "! This is your day number " + str(count) + " with us! Thank you for being here!"
print(msg)

print()

# Option 2
msg = "Hello {}! This is your day number {} with us! Thank you for being here!"
print(msg.format(name, count))
print()

# Option 3
msg = f"Hello {name}! This is your day number {count} with us! Thank you for being here!"
print(msg)

print()
print("-" * 20 + "VARIABLE TYPES" + "-" * 20)

var_int = 1 # int, integer
var_str = "Hello Jakub!" # str, string
var_float = 2.5 # float
var_bool = True # bool, boolean

print(var_int, type(var_int))
print(var_str, type(var_str))
print(var_float, type(var_float))
print(var_bool, type(var_bool))
