def move_readers(readers):
    buffer = []
    for reader in readers:
        buffer.append(next(reader))
    return ''.join(buffer)
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
    res = 0
    readers = []
    for line in file:
        if line[0] == '*' or line[0] == '+':
            operations_line = line.rsplit(' ')
            curr_operation_iter = iter(operations_line)
            current_numbers = []

            current_operation = next(curr_operation_iter)
            current_numbers.append(int(move_readers(readers)))
            for chr in curr_operation_iter:
                if chr == '*' or chr == '+':
                    if current_operation == '*':
                        res += mul_reduce(current_numbers)
                    else:
                        res += add_reduce(current_numbers)
                    current_operation = chr
                    current_numbers = []
                    move_readers(readers)
                    current_numbers.append(int(move_readers(readers)))
                    continue
                else: current_numbers.append(int(move_readers(readers)))
            if current_operation == '*':
                res += mul_reduce(current_numbers)
            else:
                res += add_reduce(current_numbers) 
            break
        readers.append(iter(line))
    print(res)
        
