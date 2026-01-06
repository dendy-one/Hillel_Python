date = [
    [1, 3, 5],
    [6],
    [],
    [0, 1, 7, 2, 4, 8],
]

for line in date:
    result = sum([line[num] for num in range(0, len(line), 2)])
    last_element = line[len(line) - 1] if line != [] else 0
    print(result * last_element)
