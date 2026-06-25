print("PYTHON CALCULATOR")

def add(a, b):
    return a+b


def subtract(a, b):
    return a-b


def multiply(a, b):
    return a*b


def divide(a, b):
    if b == 0:
        return "Cannot be divisible"
    else:
        return a/b


def modulus(a, b):
    return a % b


def power(a, b):
    return a**b


while True:
    print("+-------------------------+")
    print("|  Select any one option  |")
    print("+-------------------------+")
    print("|1.Addition(+)            |")
    print("|2.Subtraction(-)         |")
    print("|3.Multiplication(*)      |")
    print("|4.Division(/)            |")
    print("|5.Modulus(%)             |")
    print("|6.Power(^)               |")
    print("|7.Exit                   |")
    print("+-------------------------+")

    choice = input("Enter the choice:")

    if choice == "7":
        print("+-----------------------+")
        print("Thankyou for using the Calculator")
        print("+-----------------------+")
        break

    elif choice in ["1", "2", "3", "4", "5", "6"]:
        num1 = float(input("Enter the first number:"))
        num2 = float(input("Enter the second number:"))

    if choice == "1":
        print("\n+-----------------------+")
        print("Result:", add(num1, num2))
        print("+-----------------------+\n")
    elif choice == "2":
        print("+\n-----------------------+")
        print("Result:", subtract(num1, num2))
        print("+-----------------------+\n")
    elif choice == "3":
        print("\n+-----------------------+")
        print("Result:", multiply(num1, num2))
        print("+-----------------------+\n")
    elif choice == "4":
        print("\n+-----------------------+")
        print("Result:", divide(num1, num2))
        print("+-----------------------+\n")
    elif choice == "5":
        print("\n+-----------------------+")
        print("Result:", modulus(num1, num2))
        print("+-----------------------+\n")
    elif choice == "6":
        print("\n+-----------------------+")
        print("Result:", power(num1, num2))
        print("+-----------------------+\n")
    else:
        print("Invalid choice")
