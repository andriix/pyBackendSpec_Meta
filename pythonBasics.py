my_string = "looping"

for item in my_string:
    print("output: ", item)

for idx, item in enumerate(my_string):
    print(idx, item)

[print("output: ", item) for item in my_string]
