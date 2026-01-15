def is_palindrome(text: str) -> bool:
    """
    Перевіряє, чи є рядок паліндромом, ігноруючи регістр та не алфавітні
    символи.

    Функція приводить усі символи до нижнього регістру та видаляє все,
    що не є літерою або цифрою. Після цього порівнює очищений рядок
    з його реверсованою версією.

    Args:
        text (str): Вхідний рядок для перевірки.

    Returns:
        bool: True, якщо очищений рядок є паліндромом, інакше False.
    """
    text = "".join(char.lower() for char in text if char.isalnum())

    return text == text[::-1]


assert is_palindrome("A man, a plan, a canal: Panama") == True, "Test1"
assert is_palindrome("0P") == False, "Test2"
assert is_palindrome("a.") == True, "Test3"
assert is_palindrome("aurora") == False, "Test4"
print("ОК")
