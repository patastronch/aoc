from pandas import read_csv


def get_data(fname):
    return list(read_csv(fname, header=None)[0])


def day_01_part_1(fname):
    l = get_data(fname)
    s = 0
    for i in range(len(l) - 1):
        s += 1 if l[i + 1] - l[i] > 0 else 0
    return s


print("day 1, part 1, test ::", day_01_part_1("01_data_test"))
print("day 1, part 1 ::", day_01_part_1("01_data"))


def day_01_part_2(fname, window):
    l = get_data(fname)
    s = 0
    for i in range(len(l) - window):
        s += 1 if sum(l[i + 1 : i + 1 + window]) - sum(l[i : i + window]) > 0 else 0
    return s


print("day 1, part 2, test ::", day_01_part_2("01_data_test", 3))
print("day 1, part 2 ::", day_01_part_2("01_data", 3))
