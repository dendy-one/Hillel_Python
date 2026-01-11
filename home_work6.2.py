numbers = input("enter any numbers: ")
while len(numbers) > 1:
    result = 1

    for digits in numbers:
        result *= int(digits)

    numbers = str(result)

print(numbers)
