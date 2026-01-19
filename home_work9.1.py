def popular_words(text: str, words: list) -> list:
    """
    На вхід функції передаються два аргументи: текст та список слів,
    популярність які визначаємо.

    :param text: Вхідний текст
    :param words: Список слів для підрахунку
    :return: Словник {слово: кількість входжень}
    """
    text = text.lower().split()
    result = {}

    for word in words:
        result.setdefault(word, text.count(word))

    return result


assert popular_words(
    """When I was One I had just begun When I was Two I was nearly new """,
    ["i", "was", "three", "near"],
) == {"i": 4, "was": 3, "three": 0, "near": 0}, "Test1"

print("OK")
