from functools import reduce


HEX_CODE = {
    '0': '0000',
    '1': '0001',
    '2': '0010',
    '3': '0011',
    '4': '0100',
    '5': '0101',
    '6': '0110',
    '7': '0111',
    '8': '1000',
    '9': '1001',
    'A': '1010',
    'B': '1011',
    'C': '1100',
    'D': '1101',
    'E': '1110',
    'F': '1111'
}


def get_data(fname):
    with open(fname) as f:
        lines = f.readlines()

    bin_line = ''
    for c in lines[0].strip('\n'):
        bin_line += HEX_CODE[c]
    return bin_line


def decode(s, i):
    res = 0
    v = int(s[i:i + 3], 2)
    ver = v
    t = int(s[i + 3:i + 6], 2)
    i += 6
    if t == 4:
        l = ''
        while s[i] == '1':
            l += s[i + 1: i + 5]
            i += 5
        l += s[i + 1: i + 5]
        i += 5
        res = int(l, 2)
    else:
        r = []
        len_type = int(s[i], 2)
        i += 1
        if len_type == 0:
            length = int(s[i:i + 15], 2)
            i += 15
            cur_size = 0
            while cur_size < length:
                n_i, v, r_p = decode(s, i)
                cur_size += n_i - i
                i = n_i
                r.append(r_p)
                ver += v
        else:
            nb_pk = int(s[i:i + 11], 2)
            i += 11
            cur_pk = 0
            while cur_pk < nb_pk:
                n_i, v, r_p = decode(s, i)
                cur_pk += 1
                i = n_i
                r.append(r_p)
                ver += v
        if t == 0:
            res = sum(r)
        elif t == 1:
            res = reduce(lambda x, y: x * y, r)
        elif t == 2:
            res = min(r)
        elif t == 3:
            res = max(r)
        elif t == 5:
            res = 1 if r[0] > r[1] else 0
        elif t == 6:
            res = 1 if r[0] < r[1] else 0
        elif t == 7:
            res = 1 if r[0] == r[1] else 0
    return i, ver, res


def day_16_part_1(fname):
    s = get_data(fname)
    _, v, _ = decode(s, 0)
    return v


print("day 16, part 1, test ::", day_16_part_1("16_data_test"))
print("day 16, part 1 ::", day_16_part_1("16_data"))


def day_16_part_2(fname):
    s = get_data(fname)
    _, _, r = decode(s, 0)
    return r


print("day 16, part 2, test ::", day_16_part_2("16_data_test"))
print("day 16, part 2 ::", day_16_part_2("16_data"))
