def second_index(text: str, some_str: str) -> int:
    """
    Повертає індекс другого входження підрядка у тексті.

    Args:
        text (str): Рядок, у якому виконується пошук.
        some_str (str): Підрядок, друге входження якого потрібно знайти.

    Returns:
        int | None: Індекс другого входження, або None, якщо його немає.
    """
    index = text.rfind(some_str)
    if not index:
        return None
    return index


assert second_index("sims", "s") == 3, "Test1"
assert second_index("find the river", "e") == 12, "Test2"
assert second_index("hi", "h") is None, "Test3"
assert second_index("Hello, hello", "lo") == 10, "Test4"

print("ОК")
