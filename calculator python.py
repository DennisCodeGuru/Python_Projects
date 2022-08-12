# Calculator
calculate = input("What to do? (+, -, *, /):" ) #tape your function

a = float(input("First number: "))
b = float(input("Second number: "))

if calculate == "+":
    c = a + b
    print("Result:" + str(c))
elif calculate == "-":
    c = a - b
    print("Result:" + str (c))
elif calculate == "*":
    c = a * b
    print("Result:" + str (c))
elif calculate == "/":
    c = a / b
    print("Result:" + str (c))
else:
    print("Wrong Number!")