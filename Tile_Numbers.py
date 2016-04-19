def tiles(x, y):
    if 1 <= x <= 4 and 1 <= y <= 4:
        return (x - 1) * 4 + y
    else:
        return 0
