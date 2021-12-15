def get_data(fname):
    with open(fname) as f:
        lines = f.readlines()
    mat = []
    instr = []
    for line in lines:
        line = line.strip("\n")
        if line == "":
            continue
        elif len(line) >= 4 and "fold" == line[0:4]:
            t_i = line.split(" ")[2].split("=")
            instr.append([t_i[0], int(t_i[1])])
        else:
            mat.append([int(i) for i in line.split(",")])
    h_max = 2 * (max([i[1] for i in mat]) + 1)
    l_max = 2 * (max([i[0] for i in mat]) + 1)
    s = []
    for i in range(h_max):
        tt = []
        for j in range(l_max):
            tt.append(0)
        s.append(tt)
    for i, j in mat:
        s[j][i] = 1
    return s, instr


def day_13_part_1(fname):
    sheet, instr = get_data(fname)
    instr = instr[0:1]
    for ins in instr:
        if ins[0] == "y":
            s_t = sheet[0 : ins[1]].copy()
            for i in range(ins[1]):
                for j in range(len(sheet[0])):
                    s_t[i][j] = max(sheet[i][j], sheet[2 * ins[1] - i][j])
            sheet = s_t.copy()
        else:
            s_t = [i[0 : ins[1]] for i in sheet.copy()]
            for i in range(len(sheet)):
                for j in range(ins[1]):
                    s_t[i][j] = max(sheet[i][j], sheet[i][2 * ins[1] - j])
            sheet = s_t.copy()
    return sum([sum(i) for i in sheet])


print("day 13, part 1, test ::", day_13_part_1("13_data_test"))
print("day 13, part 1 ::", day_13_part_1("13_data"))


def day_13_part_2(fname):
    sheet, instr = get_data(fname)
    for ins in instr:
        if ins[0] == "y":
            s_t = sheet[0 : ins[1]].copy()
            for i in range(ins[1]):
                for j in range(len(sheet[0])):
                    s_t[i][j] = max(sheet[i][j], sheet[2 * ins[1] - i][j])
            sheet = s_t.copy()
        else:
            s_t = [i[0 : ins[1]] for i in sheet.copy()]
            for i in range(len(sheet)):
                for j in range(ins[1]):
                    s_t[i][j] = max(sheet[i][j], sheet[i][2 * ins[1] - j])
            sheet = s_t.copy()
    for s in sheet:
        print("".join([" " if i == 0 else "#" for i in s]))
    return sum([sum(i) for i in sheet])


print("day 13, part 2, test ::", day_13_part_2("13_data_test"))
print("day 13, part 2 ::", day_13_part_2("13_data"))
