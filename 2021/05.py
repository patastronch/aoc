def get_data(fname):

    with open(fname) as f:
        lines = f.readlines()

    list_lines = []
    for line in lines:
        line = line.strip("\n")
        list_lines.append([[int(j) for j in i.split(",")] for i in line.split(" -> ")])

    return list_lines


def day_05_part_1(fname):

    list_lines = get_data(fname)

    results = dict()

    for l in list_lines:
        if l[0][0] == l[1][0]:
            for j in range(min(l[0][1], l[1][1]), max(l[0][1], l[1][1]) + 1):
                results[(l[0][0], j)] = results.get((l[0][0], j), 0) + 1
        elif l[0][1] == l[1][1]:
            for j in range(min(l[0][0], l[1][0]), max(l[0][0], l[1][0]) + 1):
                results[(j, l[0][1])] = results.get((j, l[0][1]), 0) + 1

    res = 0
    for i in results:
        if results[i] >= 2:
            res += 1

    return res


print("day 05, part 1, test ::", day_05_part_1("05_data_test"))
print("day 05, part 1 ::", day_05_part_1("05_data"))


def day_05_part_2(fname):

    list_lines = get_data(fname)

    results = dict()

    for l in list_lines:
        if l[0][0] == l[1][0]:
            for j in range(min(l[0][1], l[1][1]), max(l[0][1], l[1][1]) + 1):
                results[(l[0][0], j)] = results.get((l[0][0], j), 0) + 1
        elif l[0][1] == l[1][1]:
            for j in range(min(l[0][0], l[1][0]), max(l[0][0], l[1][0]) + 1):
                results[(j, l[0][1])] = results.get((j, l[0][1]), 0) + 1
        elif (l[0][0] - l[1][0]) == (l[0][1] - l[1][1]):
            for i in range(abs(l[0][0] - l[1][0]) + 1):
                results[(min(l[0][0], l[1][0]) + i, min(l[0][1], l[1][1]) + i)] = (
                    results.get(
                        (min(l[0][0], l[1][0]) + i, min(l[0][1], l[1][1]) + i), 0
                    )
                    + 1
                )
        elif (l[0][0] - l[1][0]) == -(l[0][1] - l[1][1]):
            for i in range(abs(l[0][0] - l[1][0]) + 1):
                results[(min(l[0][0], l[1][0]) + i, max(l[0][1], l[1][1]) - i)] = (
                    results.get(
                        (min(l[0][0], l[1][0]) + i, max(l[0][1], l[1][1]) - i), 0
                    )
                    + 1
                )

    res = 0
    for i in results:
        if results[i] >= 2:
            res += 1

    return res


print("day 05, part 2, test ::", day_05_part_2("05_data_test"))
print("day 05, part 2 ::", day_05_part_2("05_data"))
