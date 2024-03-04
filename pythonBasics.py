import os

current_directory = os.getcwd()

my_file_name = input("What file do I need to open:")
my_file_dir_and_name = current_directory+"/"+my_file_name

# with open(my_file_dir_and_name, 'w') as file:
#     file.writelines(["\n First line!", "\n Second line!"])
# with open(file_location_and_name, 'a') as file:
#    file.writelines(["\n First line2!", "\n Second line2!"])

try:
    print("my test txt file contains ->\n")
    with open(my_file_dir_and_name, 'r', encoding='utf-8') as my_file:
        content = my_file.readlines()
        for line in content:
            print(line)
except FileNotFoundError:
    print("The file was not found.")
except Exception as e:
    print(f"An error occurred: {e}")
