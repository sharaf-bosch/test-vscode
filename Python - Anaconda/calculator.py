
def add(a, b):
    answer = int(a)+int(b)
    print(str(a), " + ", str(b), " = ", int(answer))


def sub(a, b):
    answer = int(a)-int(b)
    print(str(a), " - ", str(b), " = ", int(answer))


def mul(a, b):
    answer = int(a)*int(b)
    print(str(a), " * ", str(b), " = ", int(answer))


def div(a, b):
    answer = int(a)/int(b)
    print(str(a), " / ", str(b), " = ", int(answer))


print("A = Addition")
print("B = Substraction")
print("C = Multiplication")
print("D = Division")
print("E = Exit the calculator")

choice = input("Please enter your operation: ")

if choice == "a" or choice == "A":
    a = input("Enter first number: ")
    b = input("Enter second number: ")
    add(a, b)

if choice == "b" or choice == "B":
    a = input("Enter first number: ")
    b = input("Enter second number: ")
    sub(a, b)

if choice == "c" or choice == "C":
    a = input("Enter first number: ")
    b = input("Enter second number: ")
    mul(a, b)

if choice == "d" or choice == "D":
    a = input("Enter first number: ")
    b = input("Enter second number: ")
    div(a, b)

if choice == "e" or choice == "E":
    print("""
    You have exited the calculator.....Please run again to start...!
    """)
    quit()
