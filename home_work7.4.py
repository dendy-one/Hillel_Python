def common_elements() -> set[int]:
    """
     Повертає множину чисел від 0 до 100,
    які одночасно діляться на 3 і на 5.

    Returns:
        set[int]: Множина спільних елементів.
    """
    return set(range(0, 101, 3)) & set(range(0, 101, 5))


assert common_elements() == {0, 75, 45, 15, 90, 60, 30}

print("OK")
