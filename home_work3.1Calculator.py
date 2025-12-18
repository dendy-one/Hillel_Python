# Користувачеві водить почерзі два числа та дію над цими числами

first_number = int(input("Enter first number: "))
second_number = int(input("Enter second number: "))
arithmetic_operation = input("Enter arithmetic operation: ")

# Обчислює результат ввода

match arithmetic_operation:
    case "+":
        print(first_number + second_number)
    case "-":
        print(first_number - second_number)
    case "*":
        print(first_number * second_number)
    case "/":
        if second_number == 0:  # Перевірку що дільник не дорівнює 0

            print("Error: division by zero")

        print(first_number / second_number)
    case _:
        print("Error: invalid operation")
