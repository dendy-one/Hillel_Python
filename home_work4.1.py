data = [
    [0, 1, 0, 12, 3],
    [0],
    [1, 0, 13, 0, 0, 0, 5],
    [9, 0, 7, 31, 0, 45, 0, 45, 0, 45, 0, 0, 96, 0],
]

for lane in data:
    non_zeros = [x for x in lane if x != 0]
    zeros_count = len(lane) - len(non_zeros)
    lane[:] = non_zeros + [0] * zeros_count
    print(lane)
