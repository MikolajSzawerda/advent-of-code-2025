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
        res += partial_res
print(res)