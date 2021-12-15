def get_data(fname):

    with open(fname) as f:
        lines = f.readlines()

    code = None
    deco = dict()
    for line in lines:
        line = line.strip("\n")
        if line == "":
            continue
        if "->" in line:
            l = line.split("->")
            deco[l[0].strip()] = l[1].strip()
        else:
            code = line

    return code, deco


def get_counts(code):
    res = dict()
    for c in code:
        res[c] = res.get(c, 0) + 1
    return res


def get_result(counts):
    c_min_val = 999999999999999999999999999999999999
    c_max_val = 0
    for i in counts:
        if c_min_val > counts[i]:
            c_min_val = counts[i]
        if c_max_val < counts[i]:
            c_max_val = counts[i]
    return c_max_val - c_min_val


def day_14_part_1(fname, n):
    code, deco = get_data(fname)
    for s in range(n):
        new_code = ""
        for i in range(len(code) - 1):
            new_code += f"{code[i]}{deco[code[i:i + 2]]}"
        new_code += code[-1]
        code = new_code

    return get_result(get_counts(code))


print("day 14, part 1, test ::", day_14_part_1("14_data_test", 10))
print("day 14, part 1 ::", day_14_part_1("14_data", 10))


def day_14_part_2(fname, n):

    code, deco = get_data(fname)

    count = dict()
    for i in range(len(code) - 1):
        count[code[i : i + 2]] = count.get(code[i : i + 2], 0) + 1

    for s in range(n):

        cur_count = dict()
        for i in count:
            cur_count[f"{i[0]}{deco[i]}"] = (
                cur_count.get(f"{i[0]}{deco[i]}", 0) + count[i]
            )
            cur_count[f"{deco[i]}{i[1]}"] = (
                cur_count.get(f"{deco[i]}{i[1]}", 0) + count[i]
            )
        count = cur_count.copy()

    final_count = dict()
    for i in count:
        final_count[i[0]] = final_count.get(i[0], 0) + count[i]
    final_count[code[-1]] = final_count.get(code[-1], 0) + 1

    return get_result(final_count)


print("day 14, part 2, test ::", day_14_part_2("14_data_test", 40))
print("day 14, part 2 ::", day_14_part_2("14_data", 40))
