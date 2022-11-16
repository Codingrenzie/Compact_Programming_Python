def sorter(sample):
    list = []
    for v in sample:
        list.append(v[1])
    list.sort()

    t = tuple(sample)
    i = 0
    for j in range(len(list)):
        for x in t:
            if x[1] == list[j]:
                sample[i] = x
                i += 1

    return print(sample)

example=[(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]

sorter(example)

