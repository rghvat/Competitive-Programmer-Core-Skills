def add_sub(a, b, c):
    # a, b, c = map(int, input().strip().split())
    total = 0
    pos = 0
    if a == b:
        if c == 0:
            return 0
        elif c == a:
            return 1
        else:
            return -1
    
    while True:
        if total == c:
            return pos
        total += a
        pos += 1
        if total == c:
            return pos
        total -= b
        pos += 1

        if total > c :
            return -1


