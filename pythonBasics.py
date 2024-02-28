file_location_and_name = 'test_file.txt'

# with open(file_location_and_name, 'w') as file:
#    file.writelines(["\n First line!", "\n Second line!"])

with open(file_location_and_name, 'a') as file:
    file.writelines(["\n First line2!", "\n Second line2!"])

try:
    with open(file_location_and_name, 'r') as file:
        content = file.read()
    print("test.file.txt contains ->", content)
except FileNotFoundError:
    print("The file was not found.")
except Exception as e:
    print(f"An error occurred: {e}")
