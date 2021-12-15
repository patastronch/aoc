from itertools import permutations


def digit_len(x):
    l_x = len(x)
    if l_x == 2:
        return {1}
    if l_x == 4:
        return {4}
    if l_x == 3:
        return {7}
    if l_x == 7:
        return {8}
    if l_x == 5:
        return {2, 3, 5}
    if l_x == 6:
        return {0, 6, 9}


def digit_inter(x, y):
    l_int = len({i for i in x}.intersection({i for i in y}))
    l_x = len(x)
    l_y = len(y)

    if l_x == 2 and l_y == 5 and l_int == 1:
        return {2, 5}
    if l_x == 2 and l_y == 5 and l_int == 2:
        return {3}
    if l_x == 2 and l_y == 6 and l_int == 1:
        return {6}
    if l_x == 2 and l_y == 6 and l_int == 2:
        return {0, 9}

    if l_x == 3 and l_y == 5 and l_int == 2:
        return {2, 5}
    if l_x == 3 and l_y == 5 and l_int == 3:
        return {3}
    if l_x == 3 and l_y == 6 and l_int == 2:
        return {6}
    if l_x == 3 and l_y == 6 and l_int == 3:
        return {0, 9}

    if l_x == 4 and l_y == 5 and l_int == 2:
        return {2}
    if l_x == 4 and l_y == 5 and l_int == 3:
        return {3, 5}
    if l_x == 4 and l_y == 6 and l_int == 3:
        return {6, 0}
    if l_x == 4 and l_y == 6 and l_int == 4:
        return {9}

    return digit_len(y)


def get_data(fname):
    with open(fname) as f:
        lines = f.readlines()
    inputs = []
    for line in lines:
        line = line.strip("\n")
        digits_tmp = line.split("|")
        digits_left = [
            "".join(sorted([j for j in i])) for i in digits_tmp[0].strip(" ").split(" ")
        ]
        digits_right = [
            "".join(sorted([j for j in i])) for i in digits_tmp[1].strip(" ").split(" ")
        ]
        inputs.append([digits_left, digits_right])
    return inputs


def day_08_part_1(fname):
    inputs = get_data(fname)
    n = 0
    for i, j in inputs:
        n += len([len(k) for k in j if len(k) in (2, 4, 3, 7)])
    return n


print("day 08, part 1, test ::", day_08_part_1("08_data_test"))
print("day 08, part 1 ::", day_08_part_1("08_data"))


def day_08_part_2(fname):
    inputs = get_data(fname)
    result = 0
    for i in range(len(inputs)):
        decode_tmp = dict()
        for j, k in permutations(inputs[i][0], 2):
            decode_tmp[k] = decode_tmp.get(
                k, {1, 2, 3, 4, 5, 6, 7, 8, 9, 0}
            ).intersection(digit_inter(j, k))
        for d in decode_tmp:
            decode_tmp[d] = decode_tmp[d].pop()
        res = ""
        for j in inputs[i][1]:
            res = f"{res}{decode_tmp[j]}"
        result += int(res)
    return result


print("day 08, part 2, test ::", day_08_part_2("08_data_test"))
print("day 08, part 2 ::", day_08_part_2("08_data"))
