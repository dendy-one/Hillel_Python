while True:
    first_number = int(input("Enter first number: "))
    second_number = int(input("Enter second number: "))
    arithmetic_operation = input("Enter arithmetic operation: ")

    match arithmetic_operation:
        case "+":
            result = first_number + second_number
        case "-":
            result = first_number - second_number
        case "*":
            result = first_number * second_number
        case "/":
            if second_number != 0:
                result = first_number / second_number
            else:
                print("Error: division by zero")
                result = None
        case _:
            print("Error: invalid operation")
            result = None

    print(f"result: {result} \n")

    answer = input("yes/y to continue: ").lower()
    if answer != "yes" and answer != "y":
        break
