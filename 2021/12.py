def get_data(fname):
    with open(fname) as f:
        lines = f.readlines()
    graph = dict()
    for i in range(len(lines)):
        s, e = lines[i].strip("\n").split("-")
        if s != "end" and e != "start":
            graph[s] = graph.get(s, set()).union({e})
        if s != "start" and e != "end":
            graph[e] = graph.get(e, set()).union({s})

    return graph


def nb_paths(cur_g, cur_v, has_time, cur_path, all_paths):
    if cur_v == "end":
        all_paths.append(cur_path)
        return 1, all_paths

    if len(cur_g[cur_v]) == 0:
        return 0, all_paths

    n = 0
    for v in cur_g[cur_v]:
        g = cur_g.copy()
        if cur_v.upper() != cur_v and cur_v != "start":
            if has_time:
                nn, all_paths = nb_paths(g, v, False, cur_path + [v], all_paths)
                n += nn
            for vv in g:
                g[vv] = g[vv].difference({cur_v})
        nn, all_paths = nb_paths(g, v, has_time, cur_path + [v], all_paths)
        n += nn
    return n, all_paths


def day_12_part_1(fname):
    all_paths = []
    graph = get_data(fname)
    _ = nb_paths(graph, "start", False, [], all_paths)
    p = set([",".join(i) for i in all_paths])
    return (len(p), len(all_paths))


print("day 12, part 1, test ::", day_12_part_1("12_data_test"))
print("day 12, part 1 ::", day_12_part_1("12_data"))


def day_12_part_2(fname):
    all_paths = []
    graph = get_data(fname)
    _ = nb_paths(graph, "start", True, [], all_paths)
    p = set([",".join(i) for i in all_paths])
    return (len(p), len(all_paths))


print("day 12, part 2, test ::", day_12_part_2("12_data_test"))
print("day 12, part 2 ::", day_12_part_2("12_data"))
