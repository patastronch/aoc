def get_data(fname):
    with open(fname) as f:
        lines = f.readlines()
    return lines


scores = {")": 3, "]": 57, "}": 1197, ">": 25137}


def day_10_part_1(fname):
    lines = get_data(fname)
    error = 0
    for line in lines:
        line = line.strip("\n")
        struct = []

        for c in line:
            if c in ("(", "[", "{", "<"):
                struct.append(c)
            else:
                l_c = struct.pop()
                if c == ")" and l_c == "(":
                    continue
                if c == "]" and l_c == "[":
                    continue
                if c == "}" and l_c == "{":
                    continue
                if c == ">" and l_c == "<":
                    continue
                error += scores[c]
                break

    return error


print("day 10, part 1, test ::", day_10_part_1("10_data_test"))
print("day 10, part 1 ::", day_10_part_1("10_data"))


scores = {"(": 1, "[": 2, "{": 3, "<": 4}


def day_10_part_2(fname):
    lines = get_data(fname)
    error = []
    for line in lines:
        line = line.strip("\n")
        struct = []
        error_l = 0
        corrupted = False
        for c in line:
            if c in ("(", "[", "{", "<"):
                struct.append(c)
            else:
                l_c = struct.pop()
                if c == ")" and l_c == "(":
                    continue
                if c == "]" and l_c == "[":
                    continue
                if c == "}" and l_c == "{":
                    continue
                if c == ">" and l_c == "<":
                    continue
                corrupted = True
                break
        if corrupted:
            continue
        struct.reverse()

        if len(struct) == 0:
            continue

        for c in struct:
            error_l = 5 * error_l + scores[c]
        error.append(error_l)

    return sorted(error)[int(len(error) / 2)]


print("day 10, part 2, test ::", day_10_part_2("10_data_test"))
print("day 10, part 2 ::", day_10_part_2("10_data"))
