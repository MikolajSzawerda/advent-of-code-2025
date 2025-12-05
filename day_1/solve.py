res = 0
with open("data/input_1.txt", "r") as file:
    x = 50
    for line in file:
        l = line.strip().split()[0]
        if l[0] == 'L':
            mov = -int(l[1:])
        else:
            mov = int(l[1:])
        x = (x + mov) % 100
        if x == 0:
            res += 1
print(res)