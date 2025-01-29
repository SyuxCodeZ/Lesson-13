# functions
def add(x, y):
    return x + y

def sub(x, y):
    return x - y

def mul(x, y):
    return x * y

def div(x, y):
    return x / y

# real calc

print("------------")
print("    CHOSE   ")
print("------------")

print("a) Addition")
print("b) Subtraction")
print("c) Multiplication")
print("d) Division")

choice = input("Enter Your Operator (a, b, c or d): ")

if choice != "a" and "b" and "c" and "d":
    print("Invalid")
    
    num1 = int(input("Enter The 1st Number: "))
    num2 = int(input("Enter The 2nd Number: "))

    if choice == "a":
        result = add(num1, num2)
        print(f"{num1} + {num2} = {result}")

    elif choice == "b":
        result = sub(num1, num2)
        print(f"{num1} - {num2} = {result}")

    elif choice == "c":
        result = mul(num1, num2)
        print(f"{num1} x {num2} = {result}")

    else:
        result = div(num1, num2)
        print(f"{num1} / {num2} = {result}")