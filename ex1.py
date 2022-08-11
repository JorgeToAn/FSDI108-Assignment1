# Imports


# Global vars
prices = [123,1,32,6453,12,457,879,65,89,0,0,1,234,1,8,9187,1,0]


# Functions
def sum_all(numbers):
    sum = 0
    count = 0
    for number in numbers:
        sum += number

        if number < 50:
            count += 1

    print("Sum:",sum)
    print("Numbers lower than 50:",count)

def print_some_nums():
    for i in range(20):
        print(i)

def list_test():
    names = []

    # add items to a list
    names.append("Bret")
    names.append("Jimmy")
    names.append("Eduardo")
    names.append("Kevin")

    # get an item
    print(names[0])
    print(names[1])
    print(names[-1]) # last on list
    print(names[-2]) # 1 before the last

def sum(a, b):
    print(float(a) + float(b))

def divide(a, b):
    if float(b) == 0:
        print("Can't divide by zero!")
    else:
        print(float(a) / float(b))

# Instructions
print("Start ex1")
# print_some_nums()
# sum_all(prices)
# list_test()

num1 = input("Please provide num1: ")
num2 = input("Please provide num2: ")
sum(num1, num2)
divide(num1, num2)