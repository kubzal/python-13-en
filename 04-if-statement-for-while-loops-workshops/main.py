# Task: Cable car gondolas for skiers going to the slope
#
# Description:
# Write a program that calculates how many gondolas are needed to transport
# a group of skiers to the slope. Each gondola can hold a maximum of 10 pairs of skis.
# The number of skiers is entered at the beginning. Each skier has between 1 and 3
# pairs of skis (randomly generated). Skiers enter the gondolas in sequence, which means
# that gondolas won't always be filled optimally. If the next skier has more ski pairs
# than there is space in the current gondola, they must take the next one.
# The program calculates how many gondolas are needed to transport all skiers to the slope.
#
# Assumptions:
# 1. The number of skiers is input at the beginning.
# 2. Each skier randomly has between 1 and 3 pairs of skis.
# 3. A gondola can carry up to 10 pairs of skis.
# 4. Skiers enter gondolas one by one, in order.
# 5. The program calculates and displays the number of gondolas needed.

import random

num_skiers = int(input("Enter the number of skiers: "))

total_ski_pairs = 0
current_ski_pairs_in_gondola = 0
gondola_count = 1

for i in range(num_skiers):
    ski_pairs = random.randint(1, 3)
    print(f"Skier number {i + 1} has {ski_pairs} pairs of skis and is entering gondola {gondola_count}")

    total_ski_pairs += ski_pairs

    if current_ski_pairs_in_gondola + ski_pairs > 10:
        print(f"Gondola {gondola_count} is full: {current_ski_pairs_in_gondola} pairs of skis")
        print()

        gondola_count += 1
        current_ski_pairs_in_gondola = ski_pairs
    else:
        current_ski_pairs_in_gondola += ski_pairs


print(f"Total number of ski pairs: {total_ski_pairs}")