print("Hello world!")

# comment

# Variables
name = "Jorge"
last_name = "Tostado"
age = 99
price = 14.56
found = False

print(name)
print(last_name)

# Math
print(3 * 12)

# String concatenation
print(name + last_name)

#Parsing
print(name + str(age))

#IF statements
if age<100:
    print("Still young")
elif age==100:
    print("Century old")
else:
    print("Maybe a little old")

#Functions
def hello():
    print("Hello there!")

def greet(name):
    print("Hello "+name+"!")

hello() # executing the function
greet("Jorge")