res = 0
with open("data/input_3.txt", "r") as file:
    for line in file:
        a, b = 0, 0
        l = line.strip().split()[0]
        for i, num in enumerate(l):
            x = int(num)
            if x > a and i != len(l) - 1:
                a, b = x, 0
            elif x > b:
                b = x
        res += a * 10 + b
print(res)