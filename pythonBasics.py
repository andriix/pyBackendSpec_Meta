"""
This pattern is particularly useful for writing Python files
that can be both used by other files as modules (imported and
reusing functions or classes defined in them) and run as
standalone scripts (executing some logic directly).
It allows for cleaner code organization and reusability,
enabling the same file to serve dual purposes without causing
side effects when imported.
"""
def useful_function():
    print("Doing something useful")

def main():
    print("Testing the useful function:")
    useful_function()

if __name__ == "__main__":
    main()

# -----------------------

class Animal:
    def speak(self):
        raise NotImplementedError("Subclass must implement abstract method")

class Dog(Animal):
    def speak(self):
        return "Woof!"

class Cat(Animal):
    def speak(self):
        return "Meow!"

class Duck(Animal):
    def noise(self):
        return "Kry kry"

my_cat = Cat()
my_cat.speak()

my_duck = Duck()
my_duck.speak()
