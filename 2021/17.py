import re


def get_data(fname):
    with open(fname) as f:
        lines = f.readlines()
    line = lines[0].strip('\n')
    x1, x2, y1, y2 = [i.strip() for i in re.sub('[^0-9\-]',' ', line).split() if i.strip() != '']
    return int(x1), int(x2), int(y1), int(y2)


def hit(x):
    return int((x + 1) * x / 2)

def day_17_part_1(fname):
    x1, x2, y1, y2 = get_data(fname)
    return hit(y1)


print("day 17, part 1, test ::", day_17_part_1("17_data_test"))
print("day 17, part 1 ::", day_17_part_1("17_data"))


def get_hits_y(v):
    r = 0
    res = []
    for i in range(10000):
        r += v - i
        res.append(r)
    return res

def get_hits_x(v):
    r = 0
    res = []
    for i in range(10000):
        if v - i >= 0:
            r += v - i
        res.append(r)
    return res


def get_touch_x(x1, x2):
    x_tg = list(range(x1, x2 + 1))
    x_touch = dict()
    for x in range(4 * abs(x2) + 4):
        l = get_hits_x(x)
        for i in range(len(l)):
            if l[i] in x_tg:
                x_touch[i + 1] = x_touch.get(i + 1, set()).union({x})
    return x_touch

def get_touch_y(y1, y2):
    y_tg = [int(i * y1 / abs(y1)) for i in range(abs(y2), abs(y1) + 1)]
    y_touch = dict()
    for y in range(2 * abs(y1) + 2):
        yy = y - abs(y1) - 1
        l = get_hits_y(yy)
        for i in range(len(l)):
            if l[i] in y_tg:
                y_touch[i + 1] = y_touch.get(i + 1, set()).union({yy})
    return y_touch

def day_17_part_2(fname):
    x1, x2, y1, y2 = get_data(fname)

    x_touch = get_touch_x(x1, x2)
    y_touch = get_touch_y(y1, y2)

    velocities = set()
    for i in range(max(max(x_touch.keys()), max(y_touch.keys()))):
        for x in x_touch.get(i, set()):
            for y in y_touch.get(i, set()):
                velocities.add((x, y))

    return len(velocities)


print("day 17, part 2, test ::", day_17_part_2("17_data_test"))
print("day 17, part 2 ::", day_17_part_2("17_data"))
