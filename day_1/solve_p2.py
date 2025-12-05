from math import ceil

# -1 R 2 -> 1
# -1 R 102 -> 2


res = 0
with open("data/input_1.test.txt", "r") as file:
    x = 50
    for line in file:
        l = line.strip().split()[0]
        if l[0] == 'L':
            zero_dist = x
            mov = -int(l[1:])
        else:
            zero_dist = 100 - x
            mov = int(l[1:])
        dist = ceil(max(abs(mov)-zero_dist, 0) / 100)
        res += abs(dist)
        x = (x + mov) % 100
        print(res, x)
print(res)
# res = 0
# with open("data/input_1.txt", "r") as file:
#     x = 50
#     for line in file:
#         l = line.strip().split()[0]
#         num = int(l[1:])
#         if l[0] == 'L':
#             direction = -1
#         else:
#             direction = 1
#         for _ in range(num):
#             x = (x + direction) % 100
#             if x == 0:
#                 res += 1
# print(res)