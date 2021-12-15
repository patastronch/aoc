from pandas import read_csv


def get_data(fname):
    d = read_csv(fname, header=None)[0]
    m = max([len(str(i)) for i in list(d)])
    return list(d.apply(lambda x: str(x).zfill(m))), m


def day_03_part_1(fname):
    l, m = get_data(fname)
    n = len(l) / 2.0
    gamma = ""
    for j in range(m):
        gamma += "1" if sum([int(i[j]) for i in l]) >= n else "0"

    val_gamma = sum(
        [
            (int(gamma[i]) * 2) ** (m - 1 - i) if i != m - 1 else int(gamma[i])
            for i in range(len(gamma))
        ]
    )

    epsilon = "".join(["1" if i == "0" else "0" for i in gamma])
    val_epsilon = sum(
        [
            (int(epsilon[i]) * 2) ** (m - 1 - i) if i != m - 1 else int(epsilon[i])
            for i in range(len(epsilon))
        ]
    )

    return val_gamma * val_epsilon


print("day 3, part 1, test ::", day_03_part_1("03_data_test"))
print("day 3, part 1 ::", day_03_part_1("03_data"))


def day_03_part_2(fname):
    l, m = get_data(fname)

    gamma = ""
    l_aux = l.copy()
    for j in range(m):
        n = len(l_aux) / 2.0
        gamma += "1" if sum([int(i[j]) for i in l_aux]) >= n else "0"
        l_aux = [i for i in l_aux if gamma[j] == i[j]]
        if len(l_aux) == 1:
            break
    oxy = l_aux[0]
    val_oxy = sum(
        [
            (int(oxy[i]) * 2) ** (m - 1 - i) if i != m - 1 else int(oxy[i])
            for i in range(len(oxy))
        ]
    )

    epsilon = ""
    l_aux = l.copy()
    for j in range(m):
        n = len(l_aux) / 2.0
        epsilon += "1" if sum([int(i[j]) for i in l_aux]) < n else "0"
        l_aux = [i for i in l_aux if epsilon[j] == i[j]]
        if len(l_aux) == 1:
            break
    co2 = l_aux[0]
    val_co2 = sum(
        [
            (int(co2[i]) * 2) ** (m - 1 - i) if i != m - 1 else int(co2[i])
            for i in range(len(co2))
        ]
    )

    return val_oxy * val_co2


print("day 3, part 2, test ::", day_03_part_2("03_data_test"))
print("day 3, part 2 ::", day_03_part_2("03_data"))
