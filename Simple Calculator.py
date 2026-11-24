while True:
    a = int(input("Enter a number:"))
    b = int(input("Enter a number:"))

    def add(a,b):
        sum = a+b
        print("Sum of two numbers is:",sum)

    def subtract(a,b):
        diff = a-b
        print("Difference of two numbers is:",diff)

    def multiply(a,b):
        product = a*b
        print("Product of two numbers is:",product)

    def division(a,b):
        if b!=0:
            quotient = a/b
            print("Quotient of two numbers is:",quotient)
        else:
            print("Cannot divide by zero")

    c = input("Enter operation to perform (add, subtract, multiply, divide): ")

    if c=="add":
        add(a,b)
    elif c=="subtract":
        subtract(a,b)
    elif c=="multiply":
        multiply(a,b)
    elif c=="divide":
        division(a,b)
    else:
        print("Invalid operation")

    choice = input("Do you want to continue? (yes/no): ")

    if choice.lower() == "no":
        break

print("Calculator stopped.")

    
