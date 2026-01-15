def add_one(some_list: list) -> list:
    """
    Збільшує на одиницю число, подане у вигляді списку цифр.

    Функція сприймає вхідний список як послідовність цифр, що утворюють
    невід’ємне ціле число. Вона перетворює список на число, додає 1
    та повертає новий список цифр, який представляє отримане число.

    Args:
        some_list (list): Список цілих чисел від 0 до 9, кожне з яких є цифрою.

    Returns:
        list: Новий список цифр, що представляє число, збільшене на одиницю.


    """
    number = int("".join(map(str, some_list))) + 1
    newList = [int(num) for num in str(number)]
    return newList


assert add_one([1, 2, 3, 4]) == [1, 2, 3, 5], "Test1"
assert add_one([9, 9, 9]) == [1, 0, 0, 0], "Test2"
assert add_one([0]) == [1], "Test3"
assert add_one([9]) == [1, 0], "Test4"
print("OK")
