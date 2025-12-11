# 1 квадрат числа

print(int(input("Enter a number: ")) ** 2)
print()

# 2 Середнє трьох чисел

first_number = int(input("Enter a number: "))
second_number = int(input("Enter another number: "))
third_number = int(input("Enter third number: "))
print(
    "The average of three numbers ", (first_number + second_number + third_number) / 3
)
print()

# 3 Перетворення хвилин у години”

hous, minut = divmod(int(input("Enter minutes: ")), 60)
print(f" {hous} hour, {minut}  minutes")
print()

# 4 Розрахунок знижки

product_price = int(input("Enter product price: "))
discount_price = int(input("Enter discount price: "))
print(f"discounted price: {product_price-((product_price * discount_price)//100)}")
print()

# 5 Остання цифра числа
print(f"the last digit of a number: {int(input("Enter a number: "))%10}")
print()

# 6 Периметр прямокутника
length = int(input("Enter a length: "))
width = int(input("Enter a width: "))
print(f"Perimeter of a rectangle: {length*width}")
print()

# 7 Виведення числа в стовпчик

number = int(input("Enter a number: "))
print(f"{number//1000}\n{(number//100)%10}\n{(number//10)%10}\n{(number%10)}")
print()
