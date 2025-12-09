
from copy import deepcopy
def replace(str, idx, val):
    return str[:idx] + val + str[idx+1:]
with open('data/input_7.txt', 'r') as file:
    reader = iter(file)
    first_line = next(reader)
    max_right = len(first_line)
    start_idx = first_line.find('S')
    data = set([start_idx])
    res = 0
    # viz = [first_line]
    while (line := next(reader, None)) is not None:
        temp_data = set()
        # viz_line = deepcopy(line)
        for idx in data:
            if line[idx] == '^':
                if idx - 1 >= 0:
                    temp_data.add(idx-1)
                    # viz_line = replace(viz_line, idx-1, '|')
                if idx + 1 < max_right:
                    temp_data.add(idx+1)
                    # viz_line = replace(viz_line, idx+1, '|')
                res += 1
            else:
                temp_data.add(idx)
                # viz_line = replace(viz_line, idx, '|')
        data = temp_data
        # viz.append(viz_line)
print(res)
# print('\n'.join(viz))