import random

date = [
    [random.randint(1, 100) for i in range(random.randint(3, 10))]
    for j in range(random.randint(3, 5))
]

for lein in date:
    my_list = [lein[0], lein[2], lein[-2]]
    print(my_list)
