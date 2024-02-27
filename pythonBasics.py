# Starter code
items = [1,2,3,4,5]
try:
    item = items[6]
    print(item)
except IndexError as e:
    print("Item does not exist in the list")

# Starter code
def divide_by(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return 0
    except Exception as exc:
        print(exc, 'Something went wrong!')

ans = divide_by(40, 0)
print(ans)

# Starter code
try:
    with open('file_does_not_exist.txt', 'r') as file:
        print(file.read())
except FileNotFoundError as e:
    print("The file could not be found")
