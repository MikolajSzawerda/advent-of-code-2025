res = 0

def inc_to_end(idxs, start_idx, new_idx):
    num = 0
    for i in range(start_idx, 12):
        idxs[i] = new_idx + num
        num += 1
    return idxs


with open("data/input_3.txt", "r") as file:
    for line in file:
        l = line.strip().split()[0]
        idxs = [i for i in range(12)]
        l_len = len(l)
        for battery_idx, num_str in enumerate(l):
            num = int(num_str)

            for current_battery_idx in range(12):
                current_battery_num = int(l[idxs[current_battery_idx]])
                if num > current_battery_num and 11 - current_battery_idx + battery_idx < l_len and battery_idx > idxs[current_battery_idx]:
                    idxs = inc_to_end(idxs, current_battery_idx, battery_idx)
                    break
        #print(''.join(l[idxs[i]] for i in range(12)))
        res += sum(int(l[idxs[i]])* 10**(11-i) for i in range(12))
print(res)
