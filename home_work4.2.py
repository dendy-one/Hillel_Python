date = [
    [1, 3, 5],
    [6],
    [],
    [0, 1, 7, 2, 4, 8],
]

for lane in date:
    result = sum([lane[num] for num in range(0, len(lane), 2)])
    last_element = lane[len(lane) - 1] if lane != [] else 0
    print(result * last_element)
