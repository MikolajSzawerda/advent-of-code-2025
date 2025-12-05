res = 0
with open("data/input_2.txt", "r") as file:
    lines = ''.join(file.readlines())
    lines = lines.split(',')
    for line in lines:
        line = line.split('-')
        start, end = int(line[0]), int(line[1])
        for i in range(start, end + 1):
            x = str(i)
            
            # for k in range(1, len(x)//2 + 1):
            #     if len(x.replace(x[:k], '')) == 0:
            #         res += int(x)
            #         break
        
print(res)