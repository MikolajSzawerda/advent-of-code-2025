with open("data/input_5.txt", "r") as file:
    intervals = []
    while (line := file.readline()) != '\n':
        a, b = line.strip().split('-')
        intervals.append((int(a),int(b)))
    
    intervals.sort(key=lambda x: x[0])

    curr_start, curr_end = intervals[0]
    res = 0
    for interval in intervals[1:]:
        start, end = interval
        if start <= curr_end + 1:
            curr_end = max(curr_end, end)
        else:
            res += (curr_end-curr_start+1)
            curr_start, curr_end = start, end
    res += (curr_end-curr_start+1)
print(res)
