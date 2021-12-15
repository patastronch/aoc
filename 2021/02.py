from pandas import read_csv


def get_data(fname):
    return read_csv(fname, header=None, sep=" ")


def day_02_part_1(fname):
    df = get_data(fname)

    h_pos = 0
    d_pos = 0
    for _, r in df.iterrows():
        h_pos += int(r[1]) if r[0] == "forward" else 0
        d_pos += int(r[1]) if r[0] == "down" else 0
        d_pos -= int(r[1]) if r[0] == "up" else 0
    return h_pos * d_pos


print("day 2, part 1, test ::", day_02_part_1("02_data_test"))
print("day 2, part 1 ::", day_02_part_1("02_data"))


def day_02_part_2(fname):
    df = get_data(fname)

    aim = 0
    h_pos = 0
    d_pos = 0
    for _, r in df.iterrows():
        h_pos += int(r[1]) if r[0] == "forward" else 0
        d_pos += aim * int(r[1]) if r[0] == "forward" else 0
        aim += int(r[1]) if r[0] == "down" else 0
        aim -= int(r[1]) if r[0] == "up" else 0
    return h_pos * d_pos


print("day 2, part 2, test ::", day_02_part_2("02_data_test"))
print("day 2, part 2 ::", day_02_part_2("02_data"))
