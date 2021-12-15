def get_data(fname):
    chips = False
    bingos = []
    new_bingo = None
    bingo_tmp = []

    with open(fname) as f:
        lines = f.readlines()

    for line in lines:
        line = line.strip("\n")
        if chips is False:
            chips = line
            continue
        elif line != "":
            if new_bingo is True:
                bingo_tmp = []
                new_bingo = False
            bingo_tmp.append([int(i) for i in line.split(" ") if i != ""])
        elif new_bingo is None:
            new_bingo = True
        else:
            bingos.append(bingo_tmp)
            new_bingo = True
    bingos.append(bingo_tmp)

    bingos_ref = dict()
    new_bingos = []
    for n, bingo in enumerate(bingos):
        bingos_ref[n] = bingo
        new_bingos.append([bingo, n])
        new_bingos.append([[[i[j] for i in bingo] for j in range(len(bingo))], n])

    return (
        [int(i) for i in chips.split(",")],
        [[j, 0, n] for i, n in new_bingos for j in i],
        bingos_ref,
    )


def day_04_part_1(fname):
    chips, bingos, bingos_ref = get_data(fname)

    winner = False
    for c in chips:
        for b in bingos:
            if c in b[0]:
                b[1] += 1
                if b[1] == len(b[0]):
                    winner = True
                    break
        if winner:
            break
    bingo_winner = [j for i in bingos_ref[b[2]] for j in i]
    last_chip = c
    sum_rem = sum(bingo_winner)
    for c in chips:
        if c in bingo_winner:
            sum_rem -= c
        if c == last_chip:
            break
    return sum_rem * last_chip


print("day 4, part 1, test ::", day_04_part_1("04_data_test"))
print("day 4, part 1 ::", day_04_part_1("04_data"))


def day_04_part_2(fname):
    chips, bingos, bingos_ref = get_data(fname)

    winner = False
    winners = []
    for c in chips:
        for b in bingos:
            if c in b[0] and b[2] not in winners:
                b[1] += 1
                if b[1] == len(b[0]):
                    winners.append(b[2])
                    if len(winners) == len(bingos_ref):
                        winner = True
                        break
        if winner:
            break

    bingo_winner = [j for i in bingos_ref[winners[-1]] for j in i]
    last_chip = c
    sum_rem = sum(bingo_winner)
    for c in chips:
        if c in bingo_winner:
            sum_rem -= c
        if c == last_chip:
            break
    return sum_rem * last_chip


print("day 4, part 2, test ::", day_04_part_2("04_data_test"))
print("day 4, part 2 ::", day_04_part_2("04_data"))
