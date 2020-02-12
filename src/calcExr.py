#Простой калькулятор

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y

while True:
    print("Select an option: ")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("'quit' to end the program")

    #taking input, add try except
    user_choice = input("Enter 1, 2, 3, 4 or quit: ")

    if user_choice == "quit":
        break

    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    if user_choice == "1":
        print(num1, "+", num2, "=", add(num1, num2))
    elif user_choice == "2":
        print(num1, "-", num2, "=", subtract(num1, num2))
    elif user_choice == "3":
        print(num1, "*", num2, "=", multiply(num1, num2))
    elif user_choice == "4":
        print(num1, "/", num2, "=", divide(num1, num2))
    else:
        print("Unknown input")
