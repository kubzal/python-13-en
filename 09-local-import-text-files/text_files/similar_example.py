

list_a = [1, 2, 3]

number_from_a_user = [4, 5, 6]

# option 1
# 1. read list_a

list_b = list()
# rewriting the list_a into list_b
for index, number in enumerate(list_a):
    list_b[index] = list_a[index]

# adding new items from number_from_a_user
for index, number in enumerate(number_from_a_user):
    list_b[len(list_a) + index] = list_a[index]

# option 2
list_b = list_a
for number in number_from_a_user:
    list_b.append(number)
