first_list = [1, 2, 3, 4, 5, 6]
second_list = [1, 2, 3]
third_list = [1]
forth_list = [1, 2, 3, 4, 5]
fifth_list = []

print(
    first_list[: (len(first_list) + 1) // 2], first_list[(len(first_list) + 1) // 2 :]
)
print(
    second_list[: (len(second_list) + 1) // 2],
    second_list[(len(second_list) + 1) // 2 :],
)
print(
    third_list[: (len(third_list) + 1) // 2], third_list[(len(third_list) + 1) // 2 :]
)
print(
    forth_list[: (len(forth_list) + 1) // 2], forth_list[(len(forth_list) + 1) // 2 :]
)
print(
    fifth_list[: (len(fifth_list) + 1) // 2], fifth_list[(len(fifth_list) + 1) // 2 :]
)
