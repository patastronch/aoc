def get_data(fname):
    with open(fname) as f:
        lines = f.readlines()
    return [int(i) for i in lines[0].strip("\n").split(",")]


def day_07_part_1(fname):
    pos = get_data(fname)
    p_min = min(pos)
    p_max = max(pos)
    v_min = 10000000000000000
    for p in range(p_min, p_max + 1):
        v_cur = sum([abs(i - p) for i in pos])
        if v_cur < v_min:
            v_min = v_cur

    return v_min


print("day 07, part 1, test ::", day_07_part_1("07_data_test"))
print("day 07, part 1 ::", day_07_part_1("07_data"))


def day_07_part_2(fname):
    pos = get_data(fname)
    p_min = min(pos)
    p_max = max(pos)
    v_min = 10000000000000000
    for p in range(p_min, p_max + 1):
        v_cur = sum([(abs(i - p)) * (abs(i - p) + 1) / 2 for i in pos])
        if v_cur < v_min:
            v_min = v_cur

    return int(v_min)


print("day 07, part 2, test ::", day_07_part_2("07_data_test"))
print("day 07, part 2 ::", day_07_part_2("07_data"))
