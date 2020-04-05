def erasing_maximum(lst):
    # input()
    # lst = list(map(int, input().strip.split()))
    maximum = max(lst)
    indexes = []

    for index, value in enumerate(lst):
        if value == maximum:
            indexes.append(index)

    if len(indexes) > 1:
        del lst[indexes[2]]
    else:
        del lst[indexes[0]]

    #print(lst)
    return lst
