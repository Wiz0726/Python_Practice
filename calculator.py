# This is a program for basic math calculations

def calculator(option):
    number1 = float(input("Enter first number: "))
    number2 = float(input("Enter second number: "))

    if option == 1:
        sum = (number1 + number2)
        print("The sum of ", number1, "and", number2, "is", sum)
    elif option == 2:
        sub = (number1 - number2)
        print("The subtraction of ", number1, "and", number2, "is", sub)
    elif option == 3:
        mult = (number1 * number2)
        print("The multiplication of ", number1, "and", number2, "is", mult)
    elif option == 4:
        div = (number1 / number2)
        print("The division of ", number1, "and", number2, "is", div)
    else:
        print("Please enter a valid option.")

print("1 - Addition")
print("2 - Subtraction")
print("3 - Multiplication")
print("4 - Division")
choice = int(input("Select an option: "))
calculator(choice)