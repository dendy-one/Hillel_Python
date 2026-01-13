def say_hi(name: str, age: int) -> str:
    """
      Формує привітальне повідомлення з ім'ям та віком.

    Args:
        name (str): Ім'я людини.
        age (int): Вік людини.

    Returns:
        str: Рядок з привітанням у форматі:
             "Hi. My name is <name> and I'm <age> years old"
    """
    return f"Hi. My name is {name} and I'm {age} years old"


assert say_hi("Alex", 32) == "Hi. My name is Alex and I'm 32 years old", "Test1"
assert say_hi("Frank", 68) == "Hi. My name is Frank and I'm 68 years old", "Test2"

print("ОК")
