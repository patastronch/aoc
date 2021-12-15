from functools import reduce


def get_data(fname):
    with open(fname) as f:
        lines = f.readlines()
    mat = []
    for line in lines:
        line = line.strip("\n")
        mat.append([int(i) for i in line])
    return mat


def get_neighs(i, j, mat):
    neighs = []
    if i > 0:
        neighs.append(mat[i - 1][j])
    if i < len(mat) - 1:
        neighs.append(mat[i + 1][j])
    if j > 0:
        neighs.append(mat[i][j - 1])
    if j < len(mat[0]) - 1:
        neighs.append(mat[i][j + 1])
    return neighs


def day_09_part_1(fname):
    mat = get_data(fname)
    s = 0
    for i in range(len(mat)):
        for j in range(len(mat[0])):
            current = mat[i][j]
            neighs = get_neighs(i, j, mat)
            if min(neighs) > current:
                s += 1 + current
    return s


print("day 09, part 1, test ::", day_09_part_1("09_data_test"))
print("day 09, part 1 ::", day_09_part_1("09_data"))


def colorize_basin(exp_mat, mat, i, j, n, s, f):
    if exp_mat[i][j] == -1 and mat[i][j] < 9:
        neighs = get_neighs(i, j, exp_mat)
        if f or max(neighs) == n:
            exp_mat[i][j] = n
            s += 1
            if i > 0:
                exp_mat, s = colorize_basin(exp_mat, mat, i - 1, j, n, s, False)
            if i < len(mat) - 1:
                exp_mat, s = colorize_basin(exp_mat, mat, i + 1, j, n, s, False)
            if j > 0:
                exp_mat, s = colorize_basin(exp_mat, mat, i, j - 1, n, s, False)
            if j < len(mat[0]) - 1:
                exp_mat, s = colorize_basin(exp_mat, mat, i, j + 1, n, s, False)
    return exp_mat, s


def day_09_part_2(fname):
    mat = get_data(fname)
    basins = []
    curr_basin = -1
    exp_mat = [[-1] * len(mat[0]) for i in mat]

    for i in range(len(mat)):
        for j in range(len(mat[0])):
            if exp_mat[i][j] == -1 and mat[i][j] < 9:
                curr_basin += 1
                exp_mat, cur_size = colorize_basin(
                    exp_mat, mat, i, j, curr_basin, 0, True
                )
                basins.append(cur_size)

    return reduce(lambda x, y: x * y, sorted(basins)[-3:])


print("day 09, part 2, test ::", day_09_part_2("09_data_test"))
print("day 09, part 2 ::", day_09_part_2("09_data"))
