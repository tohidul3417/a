# Built in functions
big = max("hello")
print(big)
tiny = min("hello")
print(tiny) 

# Defining a function
def names():
    print("Rakib")
    print("Sahin")
    print("Mamun")

# invoking the function
names()

# Defnining a function with a parameter
def greet(time):
    if time == "morning":
        print('Good morning')
    elif time == "evening":
        print('Good evening')
    else:
        print('Hello')

# Invoking the funciton with an argument
greet('morning')

# When a function does not return a value we call it a "void" function
# Write function that are not void
def say_hello(name):
    return "Hello " + name

say_hello('Sakib')