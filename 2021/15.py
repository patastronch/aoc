from queue import PriorityQueue


def get_data(fname):
    with open(fname) as f:
        lines = f.readlines()

    mat = []
    for line in lines:
        line = line.strip("\n")
        mat_line = []
        for i in line:
            mat_line.append(int(i))
        mat.append(mat_line)

    return mat


def get_neighs(node, mat):
    c_i, c_j = node
    neighs = []

    if c_i > 0:
        neighs.append([c_i - 1, c_j])
    if c_j > 0:
        neighs.append([c_i, c_j - 1])
    if c_j < len(mat[0]) - 1:
        neighs.append([c_i, c_j + 1])
    if c_i < len(mat) - 1:
        neighs.append([c_i + 1, c_j])

    return neighs


def get_costs(mat, node):

    distances = dict()
    for i in range(len(mat)):
        for j in range(len(mat[0])):
            distances[(i, j)] = float("inf")

    distances[node] = 0

    pq = PriorityQueue()
    pq.put((distances[node], node))

    while not pq.empty():
        (dist, u) = pq.get()
        neighs = get_neighs(u, mat)
        for i, j in neighs:
            t_dist = distances[u] + mat[i][j]
            if distances[(i, j)] is float("inf") or t_dist < distances[(i, j)]:
                distances[(i, j)] = t_dist
                pq.put((t_dist, (i, j)))
    return distances


def day_15_part_1(fname):
    mat = get_data(fname)

    costs = get_costs(mat, (0, 0))
    return costs[(len(mat) - 1, len(mat[0]) - 1)]


print("day 15, part 1, test ::", day_15_part_1("15_data_test"))
print("day 15, part 1 ::", day_15_part_1("15_data"))


def get_full_map(mat, n=5):
    full_mat_tmp = []
    for nn in range(n):
        full_mat_tmp += [
            [i + nn if i + nn <= 9 else i + nn - 9 for i in mat[j]]
            for j in range(len(mat))
        ]

    full_mat = full_mat_tmp.copy()
    for nn in range(1, n):
        full_mat = [
            full_mat[i]
            + [k + nn if k + nn <= 9 else k + nn - 9 for k in full_mat_tmp[i]]
            for i in range(len(full_mat))
        ].copy()

    return full_mat


def day_15_part_2(fname):
    mat = get_data(fname)
    full_mat = get_full_map(mat).copy()
    costs = get_costs(full_mat, (0, 0))
    return costs[(len(full_mat) - 1, len(full_mat[0]) - 1)]


print("day 15, part 2, test ::", day_15_part_2("15_data_test"))
print("day 15, part 2 ::", day_15_part_2("15_data"))
