data = [
    [0, 1, 0, 12, 3],
    [0],
    [1, 0, 13, 0, 0, 0, 5],
    [9, 0, 7, 31, 0, 45, 0, 45, 0, 45, 0, 0, 96, 0],
]

for lane in data:
    zeros_number = lane.count(0)
    lane[:] = [number for number in lane if number != 0] + [0] * zeros_number
    print(lane)
