# Користувачеві водить почерзі два числа та дію над цими числами

first_number = int(input("Enter first number: "))
second_number = int(input("Enter second number: "))
arithmetic_operation = input("Enter arithmetic operation: ")

# Перевірку на те що при діленні дільник не дорівнює 0

if arithmetic_operation == "/" and second_number == 0:
    print("Error: division by zero")
else:
    match arithmetic_operation:
        case "+":
            print(first_number + second_number)
        case "-":
            print(first_number - second_number)
        case "*":
            print(first_number * second_number)
        case "/":
            print(first_number / second_number)
        case _:
            print("Invalid operation entered")
