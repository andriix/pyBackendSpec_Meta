"""
Benefits of Using Generator Comprehensions
- Memory Efficiency;
- Laziness;
- Composability.
"""
def read_large_file(file_name):
    with open(file_name, 'r') as file:
        lines = (line.strip() for line in file)  # Generator comprehension
        for line in lines:
            # Process each line
            pass


# Assume we have a list of dictionaries representing data about users
users = [
    {"name": "Alice", "age": 30},
    {"name": "Bob", "age": 25},
    {"name": "Charlie", "age": 35}
]
# Generator to filter users above a certain age
adult_users = (user for user in users if user["age"] >= 30)

for user in adult_users:
    print(user)
