# Example: Search for a specific number in a list and
# stop the search once it's found.
numbers = [1, 3, 5, 7, 9, 2, 4, 6, 8, 10]
target = 6
print("Example for BREAK statement ->")
for idx, number in enumerate(numbers):
    if number == target:
        print(f"Found the target number: {target} on {idx+1}-th position")
        break  # Exit the loop once the target is found

#----------------------------------

# Example: Print only odd numbers from a list, skipping even numbers.
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("Example for CONTINUE statement ->")
for number in numbers:
    if number % 2 == 0:  # Check if the number is even
        continue  # Skip to the next
    print(number)  # This will only execute for odd numbers

#----------------------------------

# Example: A loop that checks for a specific condition but doesn't require action yet.
numbers = [1, 2, 3, 4, 5]
print("Example for PASS statement ->")
for number in numbers:
    if number == 3:
        pass  # Placeholder for future code.
    print(number)
