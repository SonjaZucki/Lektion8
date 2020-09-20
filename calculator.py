num_one = int(input("Please enter the first number: "))
num_two = int(input("Please enter the second number: "))
operation = input("Please choose an operation (+, -, * or /): ")

if operation == "+":
    print(num_one + num_two)
elif operation == "-":
    print(num_one - num_two)
elif operation == "*":
    print(num_one * num_two)
elif operation == "/":
    print(num_one / num_two)
else:
    print("You did not enter a valid operation.")