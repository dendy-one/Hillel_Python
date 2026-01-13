def common_elements() -> set[int]:
    """
     Повертає множину чисел від 0 до 100,
    які одночасно діляться на 3 і на 5.

    Returns:
        set[int]: Множина спільних елементів.
    """
    first_list = set(range(0, 101, 3))
    second_list = set(range(0, 101, 5))
    intersection_list = first_list.intersection(second_list)
    return intersection_list


assert common_elements() == {0, 75, 45, 15, 90, 60, 30}

print("OK")
