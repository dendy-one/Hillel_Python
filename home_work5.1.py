import keyword
import string

date = [
    "_",
    "__",
    "___",
    "3m",
    "m3",
    "get_value",
    "get value",
    "some_super_puper_value",
    "Get_value",
    "super!int",
]

for name in date:

    match name:
        case _ if name in keyword.kwlist:
            name = False

        case _ if set(name) == {"_"} and len(name) != 1:
            name = False

        case _ if name and name[0].isdigit():
            name = False

        case _ if any(el.isupper() for el in name):
            name = False

        case _ if any(el in string.punctuation and el != "_" for el in name):
            name = False

        case _ if " " in name:
            name = False

        case _:
            name = True
    print(name)
