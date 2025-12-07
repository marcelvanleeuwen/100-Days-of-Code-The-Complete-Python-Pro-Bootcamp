import random

names = input("Please give me the names, separated by spaces:\n ")

friends = names.split()   # split on spaces and put it in a list

# 1st option
random_index = random.randint(0,4)
print(friends[random_index])


# 2nd option
print(random.choice(friends))
