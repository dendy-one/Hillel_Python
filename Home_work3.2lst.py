first_list = [2, 4, 7, 11, 0, -2, 8]
second_list = [1]
third_list = []
forth_list = [12, 3, 4, 10, 8]

# перенесимо останній елемент списку з кінця на початок

print(first_list[-1:] + first_list[:-1])
print(second_list[-1:] + second_list[:-1])
print(third_list[-1:] + third_list[:-1])
print(forth_list[-1:] + forth_list[:-1])
