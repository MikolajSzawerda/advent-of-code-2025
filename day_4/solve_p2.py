matrix = []
width = 0
with open("data/input_4.txt", "r") as file:
    for line in file:
        row = [0] * len(line)
        width = len(line)-1
        for i, c in enumerate(line):
            if c == '@':
                row[i] = 1
        matrix.append(row)
height = len(matrix)-1

res = 0
memory = [(1, 2)]
while len(memory) != 0: 
    memory = []
    for row_idx in range(height+1):
        for col_idx in range(width+1):
            if matrix[row_idx][col_idx] == 0:
                continue
            height_start, height_end = max(0, row_idx-1), min(height, row_idx+1)
            width_start, width_end = max(0, col_idx-1), min(width, col_idx+1)
            partial_res = int(sum([
                matrix[square_row_idx][square_col_idx] 
                        for square_col_idx in range(width_start, width_end+1) 
                        for square_row_idx in range(height_start, height_end+1)
            ]) <= 4)
            if partial_res == 1:
                memory.append((row_idx, col_idx))
            res += partial_res
    for record in memory:
        matrix[record[0]][record[1]] = 0
print(res)