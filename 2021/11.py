def get_data(fname):
    with open(fname) as f:
        lines = f.readlines()
    for i in range(len(lines)):
        lines[i] = [int(j) for j in lines[i].strip("\n")]
    return lines


def flash(state, i, j):

    state[i][j] = 0
    if i > 0 and j > 0:
        state[i - 1][j - 1] += 1
    if i > 0:
        state[i - 1][j] += 1
    if i > 0 and j < len(state) - 1:
        state[i - 1][j + 1] += 1
    if j > 0:
        state[i][j - 1] += 1
    if j < len(state) - 1:
        state[i][j + 1] += 1
    if i < len(state) - 1 and j > 0:
        state[i + 1][j - 1] += 1
    if i < len(state) - 1:
        state[i + 1][j] += 1
    if i < len(state) - 1 and j < len(state) - 1:
        state[i + 1][j + 1] += 1
    return state


def day_11_part_1(fname, nb):
    state = get_data(fname)
    nb_flashes = 0

    for n in range(nb):

        # Inc energy
        for i in range(len(state)):
            for j in range(len(state)):
                state[i][j] += 1

        # flashes loop
        old_nb_flashes = None
        flashes = [[False for i in range(len(state[0]))] for j in range(len(state))]
        while nb_flashes != old_nb_flashes:

            old_nb_flashes = nb_flashes
            for i in range(len(state[0])):
                for j in range(len(state)):
                    if state[i][j] > 9:
                        nb_flashes += 1
                        state = flash(state, i, j)
                        flashes[i][j] = True

        for i in range(len(state[0])):
            for j in range(len(state)):
                if flashes[i][j]:
                    state[i][j] = 0
    return nb_flashes


print("day 11, part 1, test ::", day_11_part_1("11_data_test", 100))
print("day 11, part 1 ::", day_11_part_1("11_data", 100))


def day_11_part_2(fname, nb):
    state = get_data(fname)
    nb_flashes = 0

    n = 0
    stop = False
    while not stop:
        n += 1

        # Inc energy
        for i in range(len(state)):
            for j in range(len(state)):
                state[i][j] += 1

        # flashes loop
        old_nb_flashes = None
        flashes = [[False for i in range(len(state[0]))] for j in range(len(state))]
        while nb_flashes != old_nb_flashes:

            old_nb_flashes = nb_flashes
            for i in range(len(state[0])):
                for j in range(len(state)):
                    if state[i][j] > 9:
                        nb_flashes += 1
                        state = flash(state, i, j)
                        flashes[i][j] = True

        if all([all(ii) for ii in flashes]):
            stop = True
        for i in range(len(state[0])):
            for j in range(len(state)):
                if flashes[i][j]:
                    state[i][j] = 0
    return n


print("day 11, part 2, test ::", day_11_part_2("11_data_test", 100))
print("day 11, part 2 ::", day_11_part_2("11_data", 100))
