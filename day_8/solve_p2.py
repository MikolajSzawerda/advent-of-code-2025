from math import sqrt, pow, prod
def get_key(i, j):
    if i > j:
        return f'{j},{i}'
    return f'{i},{j}'

def find_set(data, x, y):
    x_c, y_c = None, None
    for c in data:
        if x_c is not None and y_c is not None:
            return x_c, y_c
        if x in c:
            x_c = c
        if y in c:
            y_c = c
    return x_c, y_c

with open('data/input_8.txt', 'r') as file:
    distances = {}
    points = []
    for line in file:
        points.append(tuple(int(x) for x in line.split(',')))
    for i, point_1 in enumerate(points):
        for j, point_2 in enumerate(points[1:], start=1):
            if i == j:
                continue
            if f'{j},{i}' in distances.keys():
                continue
            distances[get_key(i, j)] = sqrt(sum(pow(point_1[k]-point_2[k], 2) for k in range(3)))
    min_dist = sorted(list(distances.items()), key=lambda x: x[1])
    # print(f"Index build: {len(min_dist)}")
    connections = []

    for i in range(len(min_dist)):
        x = min_dist[i][0]
        p1, p2 = x.split(',')
        c_p1, c_p2 = find_set(connections, p1, p2)
        if c_p1 is None and c_p2 is None:
            connections.append(set([p1, p2]))
        elif c_p1 is not None and c_p2 is None:
            c_p1.add(p2)
        elif c_p1 is None and c_p2 is not None:
            c_p2.add(p1)
        elif c_p1 != c_p2:
            connections.remove(c_p1)
            connections.remove(c_p2)
            new_c = c_p1.union(c_p2)
            connections.append(new_c)
        if len(connections) == 1 and len(connections[0]) == len(points):
            print(points[int(p1)][0] * points[int(p2)][0])
            break


