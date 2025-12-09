
from functools import cache
with open('data/input_7.txt', 'r') as file:
    lines = file.readlines()
    first_idx = lines[0].find('S')
    max_right = len(lines[0])
    lines = lines[1:]

    @cache
    def calc_split(idx, scan_line_idx=0):
        if scan_line_idx  >= len(lines):
            return 0
        if lines[scan_line_idx][idx] == '^':
            return (
               1
               + (calc_split(idx+1, scan_line_idx+1) if idx + 1 < max_right else 0 )
               + (calc_split(idx-1, scan_line_idx+1) if idx - 1 >= 0 else 0)
            )
        return calc_split(idx, scan_line_idx+1) 
    
    print(calc_split(first_idx)+1) 

