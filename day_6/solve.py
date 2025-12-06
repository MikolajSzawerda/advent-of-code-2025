def mul_reduce(arr):
    res = 1
    for num in arr:
        res *= num
    return res

def add_reduce(arr):
    res = 0
    for num in arr:
        res += num
    return res


with open("data/input_6.txt", "r") as file:
    first_line = file.readline().strip().split()
    matrix = []
    for num in first_line:
        matrix.append([int(num)])
    res = 0
    for line in file:
        if line[0] == '*' or line[0] == '+':
            operators = line.strip().split()
            for i, operator in enumerate(operators):
                if operator == '*':
                    res += mul_reduce(matrix[i])
                elif operator == '+':
                    res += add_reduce(matrix[i])
            print(res)
            break
        num_line = line.strip().split()
        for i, num in enumerate(num_line):
            matrix[i].append(int(num))