# 1. квадрат числа

first_number = int(input("Enter a number: "))

print(int(first_number ** 2)
print()

# 2. Середнє трьох чисел

first_number = int(input("Enter a number: "))
second_number = int(input("Enter another number: "))
third_number = int(input("Enter third number: "))

average = (first_number + second_number + third_number) / 3

print(f"The average numbers: {average} ")
print()

# 3. Перетворення хвилин у години”

hours, minutes = divmod(int(input("Enter minutes: ")), 60)

print(f"{hours} hour, {minutes} minutes")
print()

# 4. Розрахунок знижки

product_price = int(input("Enter product price: "))
discount_price = int(input("Enter discount price: "))

discounted_price = product_price - ((product_price * discount_price) // 100)

print(f"discounted price: {discounted_price}")
print()

# 5. Остання цифра числа

number = int(input("Enter a number: "))

print("The last digit of a number:", number % 10)
print()

# 6. Периметр прямокутника

length = int(input("Enter a length: "))
width = int(input("Enter a width: "))

print(f"Perimeter of a rectangle: {2 * (length * width) }")
print()

# 7. Виведення числа в стовпчик

number = int(input("Enter a number: "))

print(number // 1000)
print((number // 100) % 10)
print((number // 10) % 10)
print(number % 10)
