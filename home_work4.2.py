date = [[1, 3, 5], [6], []]

for line in date:
    res = sum([line[num] for num in range(0, len(line), 2)])
    last_element = line[len(line) - 1] if line != [] else 0
    print(res * last_element)
