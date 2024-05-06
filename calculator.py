# This is a program for basic math calculations

def calculator(option):
    x = float(input("Enter first number: "))
    y = float(input("Enter second number: "))

    if option == 1:
        sum = (x + y)
        print("The sum of ", x, "and", y, "is", sum)
    elif option == 2:
        sub = (x - y)
        print("The subtraction of ", x, "and", y, "is", sub)
    elif option == 3:
        mult = (x * y)
        print("The multiplication of ", x, "and", y, "is", mult)
    elif option == 4:
        div = (x / y)
        print("The division of ", x, "and", y, "is", div)
    else:
        print("Please enter a valid option.")

print("1 - Addition")
print("2 - Subtraction")
print("3 - Multiplication")
print("4 - Division")
x = int(input("Select an option: "))
calculator(x)