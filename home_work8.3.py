def find_unique_value(some_list: list) -> list:
    """
    Повертає єдине унікальне значення зі списку.

    Функція знаходить елемент, який зустрічається у списку рівно один раз.
    Якщо таких елементів кілька, повертається перший знайдений.
    Передбачається, що у списку гарантовано існує хоча б одне унікальне значення.

    Args:
        some_list (list): Список числових значень.

    Returns:
        any: Значення, яке зустрічається у списку лише один ра"""
    number = [num for num in some_list if some_list.count(num) == 1]

    return number[0]


assert find_unique_value([1, 2, 1, 1]) == 2, "Test1"
assert find_unique_value([2, 3, 3, 3, 5, 5]) == 2, "Test2"
assert find_unique_value([5, 5, 5, 2, 2, 0.5]) == 0.5, "Test3"
assert find_unique_value([5, 5, "a", 2, 2, 2]) == "a", "Test4"
print("ОК")
