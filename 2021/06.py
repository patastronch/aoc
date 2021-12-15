def get_data(fname):
    with open(fname) as f:
        lines = f.readlines()
    return [int(i) for i in lines[0].strip("\n").split(",")]


def day_06_part_1(fname, nb_days):
    states = get_data(fname)
    nb_fishes = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    for s in states:
        nb_fishes[s] += 1

    for d in range(1, nb_days + 1):
        n = nb_fishes[0]
        nb_fishes = nb_fishes[1:] + [0]
        nb_fishes[6] += n
        nb_fishes[8] = n

    return sum(nb_fishes)


print("day 06, part 1, test ::", day_06_part_1("06_data_test", 80))
print("day 06, part 1 ::", day_06_part_1("06_data", 80))

print("day 06, part 2, test ::", day_06_part_1("06_data_test", 256))
print("day 06, part 2 ::", day_06_part_1("06_data", 256))
