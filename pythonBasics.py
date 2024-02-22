# Lists
list1 = [1, 2, 3, 4, 5]

print(list1, sep=" ")

list1.append(6)
list1.insert(0, -1)

print(list1, sep=" ")

# Tuples
my_tuple = (1, 2, 3, 4, 5)
print(type(my_tuple))

# Sets
my_set = {1, 2, 3, 4, 5}
second_set = {4, 5, 6, 7}

print(my_set.intersection(second_set))

# Dictionaries
my_dict = {1: "coffee", 2: "tea", 3: "juice"}

for key, value in my_dict.items():
    print(f"{key} -> {value}")
